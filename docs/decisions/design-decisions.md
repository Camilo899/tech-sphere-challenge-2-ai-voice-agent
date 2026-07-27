## HT-001 – Create Follow-up Case

### Decision
The `FollowUpCase` entity is the Aggregate Root.

### Why?
It represents the complete lifecycle of a postoperative follow-up.

### Alternatives considered
- Patient as Aggregate Root ❌
- ClinicalDecision as Aggregate Root ❌

### Impact
All business operations related to a follow-up are coordinated through `FollowUpCase`.