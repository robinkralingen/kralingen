<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <section>
            <h2>Edit ${recipe.name}</h2>
            <form action="${ request.route_url('dashboard.recipe.edit', recipe_id=recipe.id) }" method="POST">
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
                    ${ form.description(placeholder='description') }
                </div>
                % if form.description.errors:
                    <ul class="errors">
                        % for error in form.description.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <div class="col-6 col-12-xsmall">
                    ${ form.image_url(placeholder='image url') }
                </div>
                % if form.image_url.errors:
                    <ul class="errors">
                        % for error in form.image_url.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <div class="col-6 col-12-xsmall">
                    ${ form.category_id(placeholder='category_id') }
                </div>
                % if form.category_id.errors:
                    <ul class="errors">
                        % for error in form.category_id.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <div class="col-6 col-12-xsmall">
                    ${ form.ingredients(placeholder='ingredients') }
                </div>
                % if form.ingredients.errors:
                    <ul class="errors">
                        % for error in form.ingredients.errors:
                            <li>${ error }</li>
                        % endfor
                    </ul>
                % endif
                <ul class="actions">
                    <li><input type="submit" value="Send" class="primary" /></li>
                </ul>
            </form>
        </section>
        <a href="${request.route_url('dashboard.recipe.delete', recipe_id=recipe.id)}" class="btn btn-default">Delete</a>
    </div>
</div>
