def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')

    config.add_route('register', '/register')
    config.add_route('create.register', '/register')

    config.add_route('recipe.list', '/recipes')
    config.add_route('recipe.detail', '/recipes/{recipe_id}')

    config.add_route('dashboard.auth.login', '/dashboard/login')
    config.add_route('dashboard.auth.logout', '/dashboard/logout')

    config.add_route('dashboard.recipe.list', '/dashboard/recipes')
    config.add_route('dashboard.recipe.create', '/dashboard/recipes/create')
    config.add_route('dashboard.recipe.edit', '/dashboard/recipes/{recipe_id}')
    config.add_route('dashboard.recipe.delete',
        '/dashboard/recipes/{recipe_id}/delete')

    config.add_static_view(
        name='media',
        path=config.registry.settings['upload_dir']
    )
