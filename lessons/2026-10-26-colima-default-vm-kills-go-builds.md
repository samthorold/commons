---
address: guides/go.md
origin: samthorold/go-slow#100
signal: trap
---

Colima's default VM (2 GiB) is too small to build the Docker image of a Go app that depends on a large generated SDK package. Compiling one such package (about 120k lines, a provider's API client) peaked at about 1.4 GB in one compiler process, and the build was killed with no clear error beyond the compiler exiting. `colima start --memory 4 --cpu 4` fixed it, and later starts keep the size. Docker Desktop's default is larger, so the trap appears on moving to Colima (for instance to avoid Docker Desktop's login). A Go Guide that recommends Colima, or docker-compose for dev/prod parity, should state the VM size, or cap the compiler's parallelism in the Dockerfile.
