<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <section>
            <h2>Register</h2>
        <form action="${request.route_url('register') }" method="POST">
                <div class="col-6 col-12-xsmall">
                    <input type="text" name="name" id="name" value="" placeholder="Name" />
                </div>
                <div class="col-6 col-12-xsmall">
                    <input type="email" name="email" id="email" value="" placeholder="Email" />
                </div>
                <div class="col-6 col-12-xsmall">
                    <input type="password" name="password" id="password" value="" placeholder="Password" />
                </div>
                <div class="col-6 col-12-xsmall">
                    <input type="password" name="password-confirm" id="password-confirm" value="" placeholder="Confirm Password" />
                </div>
                <ul class="actions">
                    <li><input type="submit" value="Send" class="primary" /></li>
                </ul>
            </form>
        </section>
    </div>
<div>
