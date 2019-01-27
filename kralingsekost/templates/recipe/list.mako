<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <header>
            <h1>Recepten</h1>
            <p>Zie hier alle recepten.</p>
        </header>
        <form method="GET">
            <input type="text" name="q" placeholder="${request.GET.get('q', 'Zoek een recept')}"/>
            <select name="category">
                <option disabled selected>selecteer een categorie</option>
                % for category in categories:
                    <option value="${ category.id }">${ category.name }</option>
                % endfor
            </select>
            <input type="submit" value="Send" class="primary" />
            <a href="${request.route_url('recipe.list')}">Wis alle filters</a>
        </form>

        <section class="tiles">
            % for recipe in recipes:
                <article class="style1">
                    <span class="image">
                        <img src="${recipe.image_url}" alt="" />
                    </span>
                    <a href="${request.route_url('recipe.detail', recipe_id=recipe.id)}">
                        <h2>${recipe.name}</h2>
                        <div class="content">
                            <p>door ${recipe.author.name}</p>
                        </div>
                    </a>
                </article>
            % endfor
        </section>
    </div>
</div>
