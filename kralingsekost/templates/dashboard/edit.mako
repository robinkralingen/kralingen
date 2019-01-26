<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <section>
            <h2>Edit ${recipe.name}</h2>
            <form action="${ request.route_url('dashboard.recipe.edit', recipe_id=recipe.id) }" method="POST">
                <div class="col-6 col-12-xsmall">
                    <input type="text" name="name" id="name" value="${recipe.name}" />
                </div>
                <div class="col-6 col-12-xsmall">
                    <input type="text" name="description" id="description" value="${recipe.description}" />
                </div>
                <ul class="actions">
                    <li><input type="submit" value="Send" class="primary" /></li>
                </ul>
            </form>
        </section>
        <a href="${request.route_url('dashboard.recipe.delete', recipe_id=recipe.id)}" class="btn btn-default">Delete</a>
    </div>
</div>
