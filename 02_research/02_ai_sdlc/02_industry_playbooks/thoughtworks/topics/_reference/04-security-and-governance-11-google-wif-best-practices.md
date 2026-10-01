# Topic 04 / Ref 11: Google Workload Identity Federation Best Practices

- source_url: `https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation`
- source_type: `official Google Cloud documentation`
- authority_level: `official implementation guidance`
- publication_time: `live doc; accessed 2026-04-17`
- topic: `04 security-and-governance`

## Why This Matters

This is one of the strongest public implementation-oriented sources on non-human identity lifecycle and auditability. It moves Topic 04 from abstract identity guidance to concrete controls for federated workload identities.

## Key Facts Captured

- Google explicitly recommends enabling data access logs for the Security Token Service API and IAM API so impersonation events are auditable.
- The doc says a `serviceAccountDelegationInfo` section can help identify the subject that impersonated a service account.
- Google stresses that `google.subject` mappings must be unique in both directions so external identities can be reliably traced back from audit logs.
- The guidance also emphasizes least privilege by limiting which external identities can impersonate a service account and by constraining what each service account can access.

## Research Use

- Strongly supports Topic 04’s claim that non-human identity security must include traceability, uniqueness, and impersonation audit chains.
- Gives a concrete answer to part of the “NHI lifecycle” problem: short-lived federation plus auditable impersonation is a safer baseline than long-lived keys.
- Useful for refining the minimum control set behind “Zero Trust for agents.”

## Caveats

- Focused on Google Cloud federation rather than a cloud-neutral architecture.
- Strong on auditability and attribute mapping, weaker on incident case studies.
