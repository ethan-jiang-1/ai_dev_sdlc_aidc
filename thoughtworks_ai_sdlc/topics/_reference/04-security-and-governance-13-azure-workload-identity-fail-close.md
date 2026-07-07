# Topic 04 / Ref 13: Microsoft Entra Workload ID on AKS

- source_url: `https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview`
- source_type: `official Microsoft Learn documentation`
- authority_level: `official implementation guidance`
- publication_time: `2025-11-18 update`
- accessed_on: `2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This source adds concrete public detail on workload identity lifecycle and fail-safe behavior in a Kubernetes environment, which is directly relevant to agent runtimes deployed as workloads.

## Key Facts Captured

- Microsoft Entra Workload ID uses Kubernetes service account token projection plus OIDC federation to let workloads access Azure resources securely.
- The documentation requires the label `azure.workload.identity/use: "true"` to move pods into a `Fail Close` scenario for reliable workload identity behavior.
- The docs expose lifecycle-relevant details such as token expiration configuration and the mapping from service account annotations to workload identity.
- This is a strong public example of workload identity as a managed runtime pattern rather than secret distribution.

## Research Use

- Strengthens Topic 04’s NHI lifecycle evidence with a second cloud-specific but operationally concrete source.
- Useful for discussing fail-close behavior, projected identities, and runtime token refresh as security properties for agent workloads.
- Helps connect Zero Trust and NHI lifecycle to Kubernetes-native operating patterns.

## Caveats

- Platform-specific.
- Focuses more on workload auth than on blast-radius scoring or incident response.
