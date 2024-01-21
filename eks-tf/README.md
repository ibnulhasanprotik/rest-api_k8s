# cluster

This is top level module creates vpc, subnets and eks cluster by calling [vpc_and_subnets](../modules/vpc_and_subnets/README.md) and [eks](../modules/eks/README.md) modules.

## Summary

This module creates following resources -
- VPC
- Subnets (3 public and 3 private)
- 1 NAT Gateway per AZ with corresponding Elasic IPs
- Internet Gateway
- Public and Private Route tables
- EKS Cluster with OIDC Provider
- [EKS Managed AddOns](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html)
  - coredns
  - vpc-cni
  - kube-proxy
- EKS Managed node group