# MySQL Advanced

This project contains advanced MySQL scripts that demonstrate various database concepts and techniques.

## Tasks

0. **We are all unique!**
   - File: `0-uniq_users.sql`
   - Creates a table `users` with unique email addresses.

1. **In and not out**
   - File: `1-country_users.sql`
   - Creates a table `users` with enumerated country values.

2. **Best band ever!**
   - File: `2-fans.sql`
   - Ranks country origins of bands by the number of fans.

3. **Old school band**
   - File: `3-glam_rock.sql`
   - Lists Glam rock bands, ranked by their longevity.

4. **Buy buy buy**
   - File: `4-store.sql`
   - Creates a trigger to decrease item quantity after a new order.

5. **Email validation to sent**
   - File: `5-valid_email.sql`
   - Creates a trigger to reset the `valid_email` attribute when the email is changed.

6. **Add bonus**
   - File: `6-bonus.sql`
   - Creates a stored procedure `AddBonus` to add a new correction for a student.

7. **Average score**
   - File: `7-average_score.sql`
   - Creates a stored procedure `ComputeAverageScoreForUser` to calculate and store the average score for a student.

8. **Optimize simple search**
   - File: `8-index_my_names.sql`
   - Creates an index on the first letter of names in the `names` table.

9. **Optimize search and score**
   - File: `9-index_name_score.sql`
   - Creates an index on the first letter of names and scores in the `names` table.

10. **Safe divide**
    - File: `10-div.sql`
    - Creates a function `SafeDiv` that safely divides two numbers.

11. **No table for a meeting**
    - File: `11-need_meeting.sql`
    - Creates a view `need_meeting` that lists students needing a meeting based on their scores and last meeting date.

## Usage

To run these scripts, use the MySQL command-line client:

```bash
mysql -u username -p < script_name.sql
