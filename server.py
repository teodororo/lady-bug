from src.app import app
from src.utils.environments import env

if __name__ == '__main__':
    # if env('APP_MODE') == 'development':
    #     app.run(
    #         host=env('APP_HOST'),
    #         port=int(env('APP_PORT')),
    #         debug=True,
    #         access_log=True,
    #         workers=int(env('APP_WORKERS')),
    #         auto_reload=True
    #         )
    app.run(host="0.0.0.0", port=3000, debug=True)