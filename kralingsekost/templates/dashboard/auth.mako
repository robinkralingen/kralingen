<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <section>
            <h2>Login</h2>
            <form action="${ request.route_url('dashboard.auth.login') }" method="POST">
                <div class="col-6 col-12-xsmall">
                    ${ form.email(placeholder='Email') }
                </div>
                % if form.email.errors:
                    <ul class="errors">
                        % for error in form.email.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <div class="col-6 col-12-xsmall">
                    ${ form.password(placeholder='password') }
                </div>
                % if form.password.errors:
                    <ul class="errors">
                        % for error in form.password.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <ul class="actions">
                    <li><input type="submit" value="Send" class="primary" /></li>
                    <li><a href="${request.route_url('register')}">Registreer</a></li>
                </ul>
            </form>
        </section>
    </div>
<div>
