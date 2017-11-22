<?php

$recepient = "sania_piter@mail.ru";
$sitename = "My_test";

$name = trim($_GET["name"]);
$phone = trim($_GET["phone"]);
$text = trim($_GET["text"]);

$pagetitle = "Нова заявка з сайту \"My_test\"";
$message = "Імя: $name \nТелефон: $phone \nТекст: $text";
mail($recepient, $pagetitle, $message, "Content-type: text/plain; charset=\"utf-8\"\n From: $recepient");