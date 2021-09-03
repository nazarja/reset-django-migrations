# place in root directory of django project, i.e the same level as the manage.py file
import os
import shutil


class ResetMigrations:

    def __init__(self):
        self.cwd = os.getcwd()
        self.migrations = '/migrations'
        self.pyc = '/__pycache__'
        self.m_pyc = '/migrations/__pycache__'

    def reset_sqlite(self):
        if os.path.exists('db.sqlite3'):
            os.rename('db.sqlite3', 'db.sqlite3.old')
            file = open("db.sqlite3", "x")
            file.close()

    def delete_migrations_pycache(self):
        dirs = [dir for dir in os.listdir(self.cwd) if os.path.isdir(dir)]

        for d in dirs:
            for dir, subdirs, files in os.walk(d):
                # remove __pycache__ dir
                if dir == f'{d}{self.pyc}':
                    shutil.rmtree(f'{d}{self.pyc}')

                # remove migrations/__pycache__ dir
                if dir == f'{d}{self.m_pyc}':
                    shutil.rmtree(f'{d}{self.m_pyc}')

                # remove all migrations files
                if dir == f'{d}{self.migrations}':
                    for file in files:
                        # only f its not the __init__ file
                        if file != '__init__.py':
                            os.unlink(f'{self.cwd}/{d}/{self.migrations}/{file}')

    def make_migrations(self):
        os.system('python3 manage.py makemigrations')

    def migrate(self):
        os.system('python3 manage.py migrate')


if __name__ == '__main__':
    rd = ResetMigrations()
    rd.reset_sqlite()
    rd.delete_migrations_pycache()
    rd.make_migrations()
    rd.migrate()
