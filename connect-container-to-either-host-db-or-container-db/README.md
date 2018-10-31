#### Notes

- `docker network create -d bridge --subnet 172.25.0.0/16 isolated_nw`
- `docker network ls`
- `docker run -itd --rm --network=isolated-nw --ip=172.25.3.3 --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:latest`
- `docker run -d --rm --network=isolated_nw -e DB_USER='root' -e DB_PASS='my-secret-pw' -e DB_HOST='172.25.3.3' -p 3000:3000 app`
- `docker run -d --rm -p 3001:3000 app `