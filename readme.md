## Transactions Data Sync Service
Goal of this is to create a service that can ingest transactions, merge conflicts, and insert them into a database.


#### Project progress
1. Project Configuration (not started)
2. Core transaction logic (not started)
3. API Token authentication (not started)


#### Language Choice - Python
Reason - ORM's with postgresql

#### Approach
Given an input, parse transactions 1 by 1 - checking for duplicates.
This will be slow - but intentional as accuracy is important here.

#### Transaction Entity
```python
class Transaction():
  date Date
  month Date
  description str
  category str
  amount float
  account str 
  account_number str
  institution str
  count int

  Search index on date, amount, description
  ```

#### Conflict Strategy
Upon receiving a new transaction, query for a duplicate by
`SELECT * FROM transaction WHERE description="desc" and amount="amount" and date="date"`
If there is 1 match - update could of matched record
If there are 0 matched - Create transaction with initial count of 1

#### Database
Relational - PostgreSQL
**To connect to db locally, run**
```bash
docker compose up -d
psql -U postgres -h 0.0.0.0 --port 5432 # pwd: postgres
```

#### Python Project
Install pipx
```
brew install pipx
```

Install poetry
```
pipx install poetry
```

