<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <header>
            <h1>Welkom terug ${request.user.name}</h1>
            <h2>Mijn Recepten</h2>
        </header>
        <section class="tiles">
            % for recipe in recipes:
                <article class="style1">
                    <span class="image">
                        <img src="${recipe.image_url}" alt="" />
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
