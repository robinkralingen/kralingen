<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <header>
            <h1>Mijn Recepten.</h1>
            <p>Je eigen recepten.</p>
        </header>
        <section class="tiles">
            % for recipe in recipes:
                <article class="style1">
                    <span class="image">
                        <img src="https://static.independent.co.uk/s3fs-public/thumbnails/image/2017/09/12/11/naturo-monkey-selfie.jpg?w968h681" alt="" />
                    </span>
                    <a href="${request.route_url('dashboard.recipe.edit', recipe_id=recipe.id)}">
                        <h2>${recipe.name}</h2>
                        <div class="content">
                            <p>Ga naar recept</p>
                        </div>
                    </a>
                </article>
            % endfor
        </section>
    </div>
</div>
