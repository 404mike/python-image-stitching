<?php

class Generate_List {

  private $list = [];

  private $dates = [];

  private $num_rows = 4;

  public function __construct()
  {

    $this->dates = [
      '01' => 'Ionawr - January.jpg',
      '02' => 'Chwefror - February.jpg',
      '03' => 'Mawrth - March.jpg',
      '04' => 'Ebrill - April.jpg',
      '05' => 'Mai - May.jpg',
      '06' => 'Mehefin - June.jpg',
      '07' => 'Gorffennaf - July.jpg',
      '08' => 'Awst - August.jpg',
      '09' => 'Medi - September.jpg',
      '10' => 'Hydref - October.jpg',
      '11' => 'Tachwedd - November.jpg',
      '12' => 'Rhagfyr - December.jpg'
    ];

    $this->readJson();

    file_put_contents('../json/image_order.json', json_encode($this->list,JSON_PRETTY_PRINT));
  }


  private function readJson()
  {
    $json = file_get_contents('../json/dates_ordered.json');

    $data = json_decode($json,true);

    foreach ($data as $k => $v) {

      $years = [];
      $years[] = $k.'.jpg';
      for ($i=0; $i < $this->num_rows - 1 ; $i++) { 
        $years[] = 'blank_small.jpg';
      }

      $this->list[] = $years;


      foreach($v as $key => $value) {

        $months = [];
        $months[] = $this->dates[$key];
        for ($i=0; $i < $this->num_rows - 1 ; $i++) { 
          $months[] = 'blank_small.jpg';
        }

        $this->list[] = $months;

        $num_items = count($value);

        if($num_items < $this->num_rows) {
          $this->addSmallItems($value);
        }else{
          $this->addLargeItems($value);
        }

      }      
    } 
  }

  private function addSmallItems($items)
  {
    $num_items = count($items);

    $arr = [];

    $missing_num = $this->num_rows - $num_items;

    foreach($items as $key => $value) {
      $arr[] = $this->cleanString($value);
    }

    for ($i=0; $i < $missing_num; $i++) { 
      $arr[] = 'blank_large.jpg';
    }

    $this->list[] = $arr;

  }


  private function addLargeItems($items)
  {

    $split_arr = array_chunk($items, $this->num_rows);

    foreach($split_arr as $k => $v) {
      $num_items = count($v);


      if($num_items < $this->num_rows) {
        $this->addSmallItems($v);
      }else{
        $arr = [];
        foreach($v as $key => $value) {
          $arr[] = $this->cleanString($value);
        }

        $this->list[] = $arr;
      }

    }
  }


  private function cleanString($str)
  {
    $strArr = explode('/', $str);
    $str = end($strArr);
    return $str;
  }

}

(new Generate_List());