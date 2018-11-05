##### Notes
- `docker run -p 3001:3001 -p 9229:9229 -v $PWD:/usr/app -e PORT=3001 -e DEBUG_PORT=9229 -it --rm node/app bash`
- Host debugger inside container on `0.0.0.0` if the default connection is `127.0.0.1` so your host debugger can connect
- Have fun hijacking the response when your debug breakpoint hits (`res.send('Hijacked!')`)

