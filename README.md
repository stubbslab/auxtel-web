# auxtel-web

## Use
1. Install `docker` and `docker-compose`.
2. Clone repository and `cd` into it.
3. Configure dotenv files.
```
# ./env/swag.env
PGID=<GID of docker user>
PUID=<PIG of docker user>
TZ=<timezone>
EMAIL=<email for Letsencrypt SSL certs>
URL=<domain for SSL certs>
SUBDOMAINS=<subdomains for SSL certs>
# true excludes URL from certs
ONLY_SUBDOMAINS=<"true"|"false">
```
4. Adjust volumes in `docker-compose.yml`. The app expects the images to be at `/app/static/images`. For example,
```yaml
...
volumes:
  - ./app:/app
  - <rootdir of images on host>:/app/static/images
...
```
5. Customize `nginx` conf files as needed (see `./web`).
6. Run `docker-compose -f ./docker-compose.yml up -d`
7. (first run only) Run `docker logs -f swag` to ensure certificates provision correctly.
8. Finally, point your web browser at the correct URL and check the app is running.

## todo
- [x] autorefresh (js ajax)
- [x] markdown header
- [ ] proper logging
- [ ] Clean up backend object/class handling
  - [x] make directory structure agnostic
    - [ ] more flexibility in changing naming and directory scheme
  - [ ] possibly more efficient directory crawling
- [ ] properly split python source
  - [ ] views
  - [ ] blueprints
  - [ ] utils (classes, helper functions, etc)
- [ ] build pipeline (custom container image)
