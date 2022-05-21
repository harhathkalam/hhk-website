<?php

    if(isset($_POST['name']) && isset($_POST['email']) && isset($_POST['mobile']) && isset($_POST['comment'])){
        $name = $_POST['name'];
        $email = $_POST['email'];
        $mobile = $_POST['mobile'];
        $comment = $_POST['comment'];
        $to = "info@harhathkalam.org";
        $from = "info@harhathkalam.org";
        $body = "Name: {$name} \n Email: {$email} \n Mobile: {$mobile} \n Comment: {$comment}";
        $subject = "CONTACT - Har Hath Kalam";
        if(mail($to, $subject, $body, $from)){
            echo 1;
        }
    }


?>