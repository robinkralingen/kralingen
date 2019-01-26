<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <section>
            <h2>Create</h2>
            <form action="${ request.route_url('dashboard.recipe.create') }" method="POST">
                <div class="col-6 col-12-xsmall">
                    <input type="text" name="name" id="name" value="" placeholder="Naam gerecht" />
                </div>
                <div class="col-6 col-12-xsmall">
                    <textarea name="description" id="description" placeholder="Uitleg over het gerecht" rows="40"></textarea>
                </div>
                <ul class="actions">
                    <li><input type="submit" value="Send" class="primary" /></li>
                </ul>
            </form>
        </section>
    </div>
</div>
