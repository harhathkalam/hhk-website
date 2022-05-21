<?php
    if(isset($_POST['email'])){
        $email = $_POST['email'];
        $to = "info@harhathkalam.org";
        $from = "info@harhathkalam.org";
        $body = "Email: {$email}";
        $subject = "Subscribe - Har Hath Kalam";
        if(mail($to, $subject, $body, $from)){
            echo 1;
        }
    }

?>