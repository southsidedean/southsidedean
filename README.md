# Tom Dean

Customer Success Engineer at [Solo.io](https://www.solo.io/) · Kubernetes, service mesh & AI gateways · Linux veteran & technical educator · Chicago

I help teams succeed with cloud-native infrastructure, and I've spent over 30 years doing the work myself. I started on UNIX and Linux in the data center and moved through virtualization, cloud, Kubernetes, and service mesh. Today I work with customers on cloud connectivity and agentic AI. Before Solo.io I was a field engineer at Buoyant (Linkerd), where I wrote and co-presented [*Multi-Zone Clusters Inside and Out*](https://www.youtube.com/watch?v=WhFsYVHmg6E) at KubeCon North America 2024. Earlier, at A Cloud Guru, I co-authored the RHCSA 8 course, and I've helped build hands-on lab platforms for Kubernetes training.

Always happy to talk shop: [tom@southsidedean.com](mailto:tom@southsidedean.com)

## What I've been up to

The guides and labs from 2023 came out of my blogging and teaching: Podman, KIND, Terraform, and self-hosting on Linux. I built the Kubernetes sandboxes to experiment with and learn service mesh, gateways, and kagent. I started observability-k3d to bring observability and alerting to my home network, with kagent for AI-assisted operations. It's on hold for now, and I plan to get back to it soon.

Most of my GitHub time now goes to kodi-iptv-assistant (kia). It started as an itch to scratch with IPTV program guides. I've used Claude at work since early 2026, and kia is the project that got me my own subscription and coding with it at home. kia has also become a practical place to experiment with agentic AI, like a read-only MCP server that lets an AI assistant answer questions about your setup.

Lots of people want a media stack at home, but media stacks are a pain to set up and keep running. That kind of friction has kept me from trying plenty of cool technology over the years. kia's goal is to remove it, so you can have a working media stack in short order.

### Highlights

- [kodi-iptv-assistant](https://github.com/southsidedean/kodi-iptv-assistant) (new in Oct 2026) is a self-hosted Docker service. Every night it tests thousands of free IPTV streams, matches the working channels to program guide data, and serves a tidy playlist and guide to Kodi, Plex, Jellyfin, TiviMate, and phone apps. It runs on macOS, Linux, or a Raspberry Pi. When something's wrong, `kia doctor` (or **Ask kia what's wrong** on its dashboard) explains why.
- [istio-envoy-sandboxes](https://github.com/southsidedean/istio-envoy-sandboxes) has scripted sandboxes on k3d, kind, and AWS EKS for Istio (sidecar and ambient), kgateway, kagent AI agents, SPIFFE/SPIRE workload identity, and locality load balancing.
- [observability-k3d](https://github.com/southsidedean/observability-k3d) (on hold) runs a homelab observability stack on a local k3d cluster: Prometheus, Grafana, Loki, and UniFi metrics through Unpoller, plus kagent for AI-assisted operations.

### Recent activity

<!-- WHATS-NEW:START -->
- 2026-10-24: Released [kodi-iptv-assistant v0.5.5](https://github.com/southsidedean/kodi-iptv-assistant/releases/tag/v0.5.5)
- 2026-10-16: Created [kodi-iptv-assistant](https://github.com/southsidedean/kodi-iptv-assistant)
- 2026-04-02: Updated [istio-envoy-sandboxes](https://github.com/southsidedean/istio-envoy-sandboxes)
- 2026-04-01: Updated [observability-k3d](https://github.com/southsidedean/observability-k3d)
- 2025-09-16: Released [observability-k3d v0.1.0](https://github.com/southsidedean/observability-k3d/releases/tag/v0.1.0)
<!-- WHATS-NEW:END -->

## What I work with

- Cloud native: Kubernetes · Istio · Linkerd · Envoy · Gateway API · Helm · Docker · Podman
- AI infrastructure: kagent · agent and MCP gateways · LLM integration
- Cloud and IaC: AWS · Azure · GCP · Terraform · CloudFormation · GitLab CI/CD · GitHub Actions
- Observability: Prometheus · Grafana · Loki · Kiali
- Linux and systems: RHEL · Ubuntu · SUSE · KVM · VMware · Bash · Python · Ansible

Certifications: CKA · CKAD · AWS Certified Cloud Practitioner · Azure Fundamentals

## Guides and labs

Step-by-step tutorials from my blogging and teaching:

- Kubernetes: [Deploy KIND with Podman (macOS)](https://github.com/southsidedean/deploy-kind-using-podman-macos) · [Deploy KIND with Podman (Ubuntu)](https://github.com/southsidedean/deploy-kind-using-podman-ubuntu) · [Generate YAML manifests with kubectl](https://github.com/southsidedean/using-kubectl-generate-yaml-manifests) · [Deploy Confluence on Kubernetes](https://github.com/southsidedean/deploy-confluence-k8s-using-podman)
- Podman: [Confluence in a Podman pod](https://github.com/southsidedean/deploy-confluence-podman-pod) · [Generate and test Kubernetes manifests with Podman](https://github.com/southsidedean/using-podman-generate-test-k8s-manifest)
- Infrastructure as code: [CKA/CKAD cluster builder (Terraform + KVM)](https://github.com/southsidedean/cka-d-cluster-builder-lab) · [kubeadm cluster builder on AWS](https://github.com/southsidedean/kubeadm-cluster-builder-aws-terraform) · [Cluster API bootstrap node on AWS](https://github.com/southsidedean/cluster-api-bootstrap-node-aws-terraform) · [Hands-on with Terraform on Linux](https://github.com/southsidedean/hands-on-with-terraform-on-linux)
- Linux and self-hosting: [Self-hosted GitLab with a KVM runner](https://github.com/southsidedean/self-hosted-gitlab-libvirt) · [ZoneMinder video security](https://github.com/southsidedean/deploy-security-system-using-zoneminder) · [Multipass on macOS](https://github.com/southsidedean/intro-to-multipass-macos) · [Multipass on Ubuntu](https://github.com/southsidedean/intro-to-multipass-ubuntu)

## Resume

[PDF](https://github.com/southsidedean/southsidedean/releases/latest/download/Resume-Tom-Dean.pdf) · [Markdown](./Resume-Tom-Dean.md) · [All versions](https://github.com/southsidedean/southsidedean/releases)

## Find me

[southsidedean.com](https://southsidedean.com) · [LinkedIn](https://www.linkedin.com/in/tomdeanjr/) · [YouTube (tech)](https://www.youtube.com/@southsidedean-tech) · [YouTube (life)](https://www.youtube.com/@southsidedean-life)
