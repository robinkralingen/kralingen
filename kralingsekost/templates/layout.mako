<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <meta name="description" content="pyramid web application">
    <meta name="author" content="Pylons Project">
    <link rel="shortcut icon" href="${request.static_url('kralingsekost:static/pyramid-16x16.png')}">
    <link rel="stylesheet" href="${request.static_url('kralingsekost:static/css/main.css')}" />
    <noscript><link rel="stylesheet" href="${request.static_url('kralingsekost:static/css/noscript.css')}" /></noscript>

    <title>Kralingsekost</title>

    <!-- HTML5 shiv and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js" integrity="sha384-0s5Pv64cNZJieYFkXYOTId2HMA2Lfb6q2nAcx2n0RTLUnCAoTTsS0nKEO27XyKcY" crossorigin="anonymous"></script>
      <script src="//oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js" integrity="sha384-ZoaMbDF+4LeFxg6WdScQ9nnR1QC2MIRxA1O9KWEXQwns1G8UNyIEZIQidzb0T1fo" crossorigin="anonymous"></script>
    <![endif]-->
  </head>

  <body class="is-preload">
    <div id="wrapper">

        <!-- Header -->
          <header id="header">
            <div class="inner">

              <!-- Logo -->
                <a href="${request.route_url('recipe.list')}" class="logo">
                  <span class="title">Kralingsekost</span>
                </a>

              <!-- Nav -->
                <nav>
                  <ul>
                    <li><a href="#menu">Menu</a></li>
                  </ul>
                </nav>
            </div>
          </header>

          <nav id="menu">
            <h2>Menu</h2>
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="${request.route_url('recipe.list')}">Recepten</a></li>
              % if request.user:
                <li><a href="${request.route_url('dashboard.recipe.list')}">Mijn recepten</a></li>
                <li><a href="${request.route_url('dashboard.recipe.create')}">Recept aanmaken</a></li>
                <li><a href="${request.route_url('dashboard.auth.logout')}">Logout</a></li>
              % else:
                <li><a href="${request.route_url('dashboard.auth.login')}">Login</a></li>
              % endif
            </ul>
          </nav>

          ${next.body()}

        <footer id="footer">
            <div class="inner">
              <ul class="copyright">
              </ul>
            </div>
          </footer>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="${request.static_url('kralingsekost:static/js/jquery.min.js')}"></script>
    <script src="${request.static_url('kralingsekost:static/js/browser.min.js')}"></script>
    <script src="${request.static_url('kralingsekost:static/js/breakpoints.min.js')}"></script>
    <script src="${request.static_url('kralingsekost:static/js/util.js')}"></script>
    <script src="${request.static_url('kralingsekost:static/js/main.js')}"></script>
  </body>
</html>

