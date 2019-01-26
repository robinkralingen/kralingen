<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <section>
            <h2>Login</h2>
            <form action="${ request.route_url('dashboard.auth.login') }" method="POST">
                <div class="col-6 col-12-xsmall">
                    <input type="email" name="email" id="email" value="" placeholder="Email" />
                </div>
                <div class="col-6 col-12-xsmall">
                    <input type="password" name="password" id="password" value="" placeholder="Password" />
                </div>
                <ul class="actions">
                    <li><input type="submit" value="Send" class="primary" /></li>
                </ul>
            </form>
        </section>
    </div>
<div>
