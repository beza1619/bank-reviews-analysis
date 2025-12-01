# Database Schema Documentation

## Table: banks
| Column | Type | Constraints |
|--------|------|-------------|
| bank_id | INTEGER | PRIMARY KEY |
| bank_name | TEXT | NOT NULL |
| app_name | TEXT | NOT NULL |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

## Table: sqlite_sequence
| Column | Type | Constraints |
|--------|------|-------------|
| name |  |  |
| seq |  |  |

## Table: reviews
| Column | Type | Constraints |
|--------|------|-------------|
| review_id | TEXT | PRIMARY KEY |
| bank_id | INTEGER |  |
| review_text | TEXT | NOT NULL |
| rating | INTEGER |  |
| review_date | DATE | NOT NULL |
| sentiment_label | TEXT |  |
| sentiment_score | REAL |  |
| themes | TEXT |  |
| source | TEXT | DEFAULT 'Google Play' |
| created_at | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP |

