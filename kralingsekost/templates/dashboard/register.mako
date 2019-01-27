<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <section>
            <h2>Register</h2>
        <form action="${request.route_url('register') }" method="POST">
        <input type="hidden" name="csrf_token" value="${ request.session.get_csrf_token() }" />
                <div class="col-6 col-12-xsmall">
                    ${ form.name(placeholder='name') }
                </div>
                % if form.name.errors:
                    <ul class="errors">
                        % for error in form.name.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <div class="col-6 col-12-xsmall">
                    ${ form.email(placeholder='email') }
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
                <div class="col-6 col-12-xsmall">
                    ${ form.password_confirm(placeholder='password confirmation') }
                </div>
                % if form.password_confirm.errors:
                    <ul class="errors">
                        % for error in form.password_confirm.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <ul class="actions">
                    <li><input type="submit" value="Send" class="primary" /></li>
                </ul>
            </form>
        </section>
    </div>
<div>
