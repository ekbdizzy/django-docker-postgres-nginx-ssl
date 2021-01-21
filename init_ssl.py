import sys
from jinja2 import Environment, FileSystemLoader

LETSENCRYPT_TEMPLATE = './data/templates/template-init-letsencrypt.sh'
NGINX_TEMPLATE = './data/templates/template_project_ssl.conf'

env = Environment(loader=FileSystemLoader('.'))


def render_content(path_to_template, **kwargs):
    template = env.get_template(path_to_template)
    rendered_content = template.render(**kwargs)
    return rendered_content


if __name__ == "__main__":

    domain_name = input('Enter your domain name: ')
    if not domain_name:
        sys.exit('Domain can not be empty.')

    email = input('Input your email: ')

    with open('init-letsencrypt.sh', 'w', encoding='utf-8') as file:
        file.write(render_content(LETSENCRYPT_TEMPLATE, domain_name=domain_name, email=email))

    with open('./data/nginx/conf_ssl.d/project.conf', 'w', encoding='utf-8') as file:
        file.write(render_content(NGINX_TEMPLATE, domain_name=domain_name, email=email))
