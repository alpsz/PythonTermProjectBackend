from string import Template

verify_email = Template("""<!DOCTYPE html>
<html>

<head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <style type="text/css">
    @media screen {
        @font-face {
            font-family: 'Lato';
            font-style: normal;
            font-weight: 400;
            src: local('Lato Regular'), local('Lato-Regular'), url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff) format('woff');
        }

        @font-face {
            font-family: 'Lato';
            font-style: normal;
            font-weight: 700;
            src: local('Lato Bold'), local('Lato-Bold'), url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff) format('woff');
        }

        @font-face {
            font-family: 'Lato';
            font-style: italic;
            font-weight: 400;
            src: local('Lato Italic'), local('Lato-Italic'), url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff) format('woff');
        }

        @font-face {
            font-family: 'Lato';
            font-style: italic;
            font-weight: 700;
            src: local('Lato Bold Italic'), local('Lato-BoldItalic'), url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff) format('woff');
        }
    }

    /* CLIENT-SPECIFIC STYLES */
    body,
    table,
    td,
    a {
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
    }

    table,
    td {
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
    }

    img {
        -ms-interpolation-mode: bicubic;
    }

    /* RESET STYLES */
    img {
        border: 0;
        height: auto;
        line-height: 100%;
        outline: none;
        text-decoration: none;
    }

    table {
        border-collapse: collapse !important;
    }

    body {
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
    }

    /* iOS BLUE LINKS */
    a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
    }

    /* MOBILE STYLES */
    @media screen and (max-width:600px) {
        h1 {
            font-size: 32px !important;
            line-height: 32px !important;
        }
    }

    /* ANDROID CENTER FIX */
    div[style*="margin: 16px 0;"] {
        margin: 0 !important;
    }
    </style>
</head>

<body style="background-color: #F4F4F4; margin: 0 !important; padding: 0 !important;">
    <!-- HIDDEN PREHEADER TEXT -->
    <div
        style="display: none; font-size: 1px; color: #FEFEFE; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
        We're thrilled to have you here! Get ready to dive into your new account. </div>
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <!-- LOGO -->
        <tr>
            <td bgcolor="#30419B" align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#30419B" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#FFFFFF" align="center" valign="top"
                            style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">
                            <h1 style="font-size: 48px; font-weight: 400; margin: 2;"><img
                                    src="https://images.vexels.com/media/users/3/136170/isolated/preview/1a0fc726567fe21282676126358b795d-heart-disease-logo.png"></h1>

                            <img src="https://thumbs.gfycat.com/AdorableUnripeArrowana-size_restricted.gif" width="325" height="320"
                                style="display: block; border: 0px;" />
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#F4F4F4" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#FFFFFF" align="center"
                            style="padding: 20px 30px 40px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <h3>Activate your account</h3>
                            <p style="margin: 0;">Hi $name, you've created a new customer account at Heart Disease Classifier. All
                                you have
                                to do is activate it.</p>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor="#FFFFFF" align="left">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td bgcolor="#FFFFFF" align="center" style="padding: 20px 30px 60px 30px;">
                                        <table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td align="center" style="background-color: white">
                                                        <a href="http://127.0.0.1:5000/users/verify?token=$token"
                                                        style="background-color:#30419B ;color: #ffffff; margin-top: 10px; padding-left: 48px; padding-right: 48px;  padding-top: 10px;  padding-bottom: 10px;border: 0px;border-radius: 10px;"
                                                        target="_blank"
                                                        >
                                                            Activate Your Account
                                                        </a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor="#FFFFFF" align="left"
                            style="padding: 0px 30px 20px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <!-- <p style="margin: 0; text-align:center;"> Button not working ?</p> -->
                            <!-- <p style="margin: 0; text-align:center; color:#30419B; font-weight:600;"> <a href="#"
                            target="_blank">https://emailpaws.com/items/register/00ydayd76sahj</a></p> -->
                        </td>
                    </tr>
                    <tr>
                        <td bgcolor="#FFFFFF" align="left"
                            style="padding: 0px 30px 40px 30px; border-radius: 0px 0px 4px 4px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <p style="margin: 0;">Cheers,<br>Heart Disease Classifier Team</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>

        <tr>
            <td bgcolor="#F4F4F4" align="center" style="padding: 30px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#4E54C8" align="center"
                            style="padding: 30px 30px 30px 30px; border-radius: 4px 4px 4px 4px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 25px;">
                            <h2 style="font-size: 20px; font-weight: 400; color: #fff; margin: 0;">Need more help?</h2>
                            <p style="margin: 0;">
                                <a href="https://app.windsondispatch.com/Windson-Dispatch/contact.php" target="_blank"
                                    style="color: #fff;">We&rsquo;re here to help you out</a>
                            </p>
                            <br>
                            <a href="#"><i class="fa fa-facebook" aria-hidden="true"
                                    style="font-size:20px;color:#fff; margin:10px"></i></a>
                            <a href="#"><i class="fa fa-instagram" aria-hidden="true"
                                    style="font-size:20px;color:#fff;margin:10px"></i></a>
                            <a href="#"><i class="fa fa-youtube-play" aria-hidden="true"
                                    style="font-size:20px;color:#fff;margin:10px"></i></a>
                            <a href="#"><i class="fa fa-linkedin-square" aria-hidden="true"
                                    style="font-size:20px;color:#fff; margin:10px"></i></a>
                        </td>
                    </tr>
                    <tr>

                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td bgcolor="#F4F4F4" align="center" style="padding: 0px 10px 0px 10px;">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                    <tr>
                        <td bgcolor="#F4F4F4" align="left"
                            style="padding: 0px 30px 30px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 18px;">
                            <br>
                            <p style="margin: 0;"></p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>

</html>""")


reset_password = Template("""
<!DOCTYPE html>

<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
<title></title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css"/>
<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css"/>
<!--<![endif]-->
<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			padding: 0;
		}

		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: inherit !important;
		}

		#MessageViewBody a {
			color: inherit;
			text-decoration: none;
		}

		p {
			line-height: inherit
		}

		@media (max-width:670px) {
			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}

			.row-content {
				width: 100% !important;
			}

			.column .border {
				display: none;
			}

			table {
				table-layout: fixed !important;
			}

			.stack .column {
				width: 100%;
				display: block;
			}
		}
	</style>
</head>
<body style="background-color: #000000; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
<table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;" width="100%">
<tbody>
<tr>
<td>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f3e6f8;" width="100%">
<tbody>
<tr>
<td>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
<tbody>
<tr>
<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
<table border="0" cellpadding="0" cellspacing="0" class="image_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td style="padding-bottom:15px;padding-top:15px;width:100%;padding-right:0px;padding-left:0px;">
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f3e6f8;" width="100%">
<tbody>
<tr>
<td>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; background-image: url('https://drive.google.com/uc?id=1-YGasu626sr-vqklFfIRZFdsA1cQQ_LP&export=download'); background-position: center top; background-repeat: no-repeat; color: #000000; width: 650px;" width="650">
<tbody>
<tr>
<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 45px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
<table border="0" cellpadding="20" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td>
<div align="center">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span> </span></td>
</tr>
</table>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="20" cellspacing="0" class="image_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td>
<div align="center" style="line-height:10px"><img alt="Forgot your password?" src="https://drive.google.com/uc?id=1z28CTcwi_-9wSpetr8iMbw_LAbNI_2nO&export=download" style="display: block; height: auto; border: 0; width: 358px; max-width: 100%;" title="Forgot your password?" width="358"/></div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" class="heading_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td style="padding-top:35px;text-align:center;width:100%;">
<h1 style="margin: 0; color: #8412c0; direction: ltr; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 28px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><strong>Forgot your password?</strong></h1>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
<tr>
<td style="padding-left:45px;padding-right:45px;padding-top:10px;">
<div style="font-family: Arial, sans-serif">
<div class="txtTinyMce-wrapper" style="font-size: 12px; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; mso-line-height-alt: 18px; color: #393d47; line-height: 1.5;">
<p style="margin: 0; text-align: center; mso-line-height-alt: 27px;"><span style="font-size:18px;color:#aa67cf;">We received a request to reset your password.</span></p>
<p style="margin: 0; text-align: center; mso-line-height-alt: 27px;"><span style="font-size:18px;color:#aa67cf;">If you didn't make this request, simply ignore this email.</span></p>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="20" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td>
<div align="center">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="80%">
<tr>
<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #E1B4FC;"><span> </span></td>
</tr>
</table>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
<tr>
<td style="padding-bottom:10px;padding-left:45px;padding-right:45px;padding-top:10px;">
<div style="font-family: Arial, sans-serif">
<div class="txtTinyMce-wrapper" style="font-size: 12px; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; text-align: center; mso-line-height-alt: 18px; color: #393d47; line-height: 1.5;">
<p style="margin: 0; mso-line-height-alt: 19.5px;"><span style="font-size:13px;color:#8412c0;">If you did make this request just click the button below:</span></p>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="10" cellspacing="0" class="button_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td>
<div align="center">
<a href="F:/Lambton/Sem1/thursday/Heart-Disease-classifier/admin/recover-password.html?token=$token" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#8412c0;border-radius:0px;width:auto;border-top:1px solid #8412c0;border-right:1px solid #8412c0;border-bottom:1px solid #8412c0;border-left:1px solid #8412c0;padding-top:10px;padding-bottom:10px;font-family:'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:40px;padding-right:40px;font-size:14px;display:inline-block;letter-spacing:normal;"><span style="font-size: 16px; line-height: 2; word-break: break-word; mso-line-height-alt: 32px;"><span data-mce-style="font-size: 14px; line-height: 28px;" style="font-size: 14px; line-height: 28px;">RESET MY PASSWORD</span></span></span></a>
<p>if above button doesn't work clicl on the link below.</p>
<a>F:/Lambton/Sem1/thursday/Heart-Disease-classifier/admin/recover-password.html?token=$token</a>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
<tr>
<td style="padding-bottom:15px;padding-left:10px;padding-right:10px;padding-top:10px;">
<div style="font-family: Arial, sans-serif">
<div class="txtTinyMce-wrapper" style="font-size: 12px; font-family: 'Cabin', Arial, 'Helvetica Neue', Helvetica, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #393d47; line-height: 1.2;">
<p style="margin: 0; font-size: 14px; text-align: center;"><span style="font-size:10px;color:#aa67cf;"><span style="">If you didn't request to change your brand password, </span><span style="">you don't have to do anything. So that's easy.</span></span></p>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
<tr>
<td style="padding-bottom:20px;padding-left:10px;padding-right:10px;padding-top:10px;">
<div style="font-family: sans-serif">
<div class="txtTinyMce-wrapper" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #8412c0; line-height: 1.2; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
<p style="margin: 0; font-size: 12px; mso-line-height-alt: 14.399999999999999px;"> </p>
</div>
</div>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f3e6f8;" width="100%">
<tbody>
<tr>
<td>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
<tbody>
<tr>
<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 10px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
<table border="0" cellpadding="5" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td>
<div align="center">
<table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span> </span></td>
</tr>
</table>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
<tr>
<td>
<div style="font-family: sans-serif">
<div class="txtTinyMce-wrapper" style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #8412c0; line-height: 1.2; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
<p style="margin: 0; text-align: center; mso-line-height-alt: 14.399999999999999px;"> </p>
<p style="margin: 0; mso-line-height-alt: 14.399999999999999px;"> </p>
</div>
</div>
</td>
</tr>
</table>
<table border="0" cellpadding="10" cellspacing="0" class="social_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="social-table" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="72px">
<tr>
<td style="padding:0 2px 0 2px;"><a href="https://www.facebook.com/" target="_blank"><img alt="Facebook" height="32" src="https://drive.google.com/uc?id=1u4PmfOn3H7mj1KGYR3SciIuKMja_QtJV&export=download" style="display: block; height: auto; border: 0;" title="facebook" width="32"/></a></td>
<td style="padding:0 2px 0 2px;"><a href="https://www.twitter.com/" target="_blank"><img alt="Twitter" height="32" src="https://drive.google.com/uc?id=1Y_7whm_6tQXE08sjUtLFYrzW1ROLF_Us&export=download" style="display: block; height: auto; border: 0;" title="twitter" width="32"/></a></td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tbody>
<tr>
<td>
<table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;" width="650">
<tbody>
<tr>
<td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
<table border="0" cellpadding="0" cellspacing="0" class="icons_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td style="vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;">
<table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
<tr>
<td style="vertical-align: middle; text-align: center;">
<!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
<!--[if !vml]><!-->
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table><!-- End -->
</body>
</html>
""")