<%inherit file="../layout.mako"/>

<div id="main">
    <div class="inner">
        <h1>${recipe.name}</h1>
        <h2>Categorie: ${recipe.category.name}</h2>
        <span class="image main"><img src="${recipe.image_url}" alt="" /></span>
        <p>${recipe.description}</p>

        <p>Recept geplaatst door: ${recipe.author.name}</p>
    </div>
</div>
