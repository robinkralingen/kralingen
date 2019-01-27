<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <header>
            <h1>Welkom terug ${request.user.name}</h1>
            <h2>Admin omgeving</h2>
        </header>
        <div class="table-wrapper">
            <table class="alt">
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>Recept</th>
                        <th>Auteur</th>
                        <th>Zichtbaarheid</th>
                        <th>Acties</th>
                    </tr>
                </thead>
                <tbody>
                    % for recipe in recipes:
                        <tr>
                            <td>${recipe.id}</td>
                            <td>${recipe.name}</td>
                            <td>${recipe.author.name}</td>
                            <td>${'hidden' if recipe.hidden else 'zichtbaar'}</td>
                            <td>
                                <form action="${ request.route_url('admin.recipe.toggle', recipe_id=recipe.id) }" method='POST'>
                                    <input type="submit" value="Toggle visibility" class="primary" />
                                </form>
                            </td>
                        </tr>
                    % endfor
                </tbody>
            </table>
        </div>
    </div>
</div>
