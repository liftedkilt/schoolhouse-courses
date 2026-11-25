# Schoolhouse courses

Course packages for Schoolhouse, a mastery-based math tutor for families. Each directory is one course: data only (a manifest, a skill graph, problem templates and the wording of worked steps and hints), with no code.

| Course | Version | What it covers | Needs first |
|---|---|---|---|
| [`ratio_percent`](ratio_percent) | 0.2.0 | Ratio and rate, percent, and money: tax, tips, discounts, simple interest (18 skills) | Arithmetic: decimals and dividing fractions |
| [`cooking`](cooking) | 0.1.0 | Kitchen measures, scaling recipes, cooking times and oven temperatures, cost and nutrition (29 skills) | Arithmetic: multiplying and dividing fractions; Ratio and percent, unit 1 |
| [`household`](household) | 0.1.0 | Shopping, pay, budgets, bills and the home, sewing and fabric, borrowing and saving (28 skills) | All of Ratio and percent |

## Installing a course

1. Open the [Releases](../../releases) page and find the course (`course-<id>-v<version>`).
2. In Schoolhouse, go to **Parents › Courses**. Either paste the link to the release's `.zip` into **Install from link**, or download the zip and use **Choose a course file…**.
3. Add the course to a child's learning path on their **Settings** tab. The "Home: cooking and household" track sets up arithmetic, ratio and percent, cooking and household in order.

Schoolhouse checks the whole file before installing anything. Installing a newer version of a course updates it and keeps every child's progress.

## About the content

- Every problem is generated from a template and checked by code, so answers are always right. Explanations and hints are written for this project (`source: own`).
- Any real-world figure a problem uses (a tax rate, the 7.65% payroll tax, a daily value) is quoted in the problem, so a learner is never marked on knowing it.
- Nutrition problems are arithmetic only; they give no dietary advice.

## Licence

[PolyForm Noncommercial 1.0.0](LICENSE.md): free for families, schools and other noncommercial use.
