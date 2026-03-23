# E-Commerce Price Intelligence

Collecting product data through web scraping and analyzing pricing patterns across categories — built as a complete data collection-to-insight pipeline.

---

## Data Collection

Data was scraped from [webscraper.io test e-commerce site](https://webscraper.io/test-sites/e-commerce/static) — a legal, publicly available practice site that mimics real marketplace HTML structure. No static CSV was used; the dataset was built from scratch using a custom scraping script.

| Attribute | Detail |
|-----------|--------|
| Source | webscraper.io (practice e-commerce site) |
| Categories scraped | Laptops, Tablets, Phones |
| Total products | [FILL: e.g. 319 products] |
| Fields collected | product_name, price, description, reviews, category |
| Scraping tool | Python · BeautifulSoup · Requests |

---

## Tools

- **Scraping:** Python, BeautifulSoup, Requests
- **Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Environment:** Jupyter Notebook

---

## Workflow

This project covers the full analyst workflow — from raw HTML to business insight.

**1. Scraping** — Custom script targets product listings across 3 categories and exports raw data to CSV.

**2. Cleaning** — Removed duplicates, standardized price format (stripped `$` symbol, cast to float), handled missing review counts.

**3. Analysis** — Price distribution per category, review volume vs price relationship, category-level comparison.

---

## Key Findings

**Laptops are the highest-priced category** — average price of $[FILL] compared to $[FILL] for Phones and $[FILL] for Tablets.

**Price and reviews have an inverse relationship.** Products priced below $[FILL] collect significantly more reviews than premium ones. This is consistent across all three categories — cheaper products move faster and generate more user feedback.

**Most products cluster in the mid-range.** The $[FILL]–$[FILL] price band has the highest product count across all categories, with few true budget or premium outliers.

---

## Visuals

![Price Distribution by Category](visuals/price_distribution.png)
![Price vs Reviews](visuals/price_vs_reviews.png)
![Category Comparison](visuals/category_comparison.png)

---

## Project Structure
```
ecommerce-price-analysis/
│
├── data/
│   └── ecommerce_data.csv        # Scraped dataset
│
├── scraper/
│   └── scraper.py                # Web scraping script
│
├── notebook/
│   └── price_analysis.ipynb      # Full analysis notebook
│
├── visuals/
│   ├── price_distribution.png
│   ├── price_vs_reviews.png
│   └── category_comparison.png
│
└── README.md
```

---

## How to Run
```bash
# Clone the repo
git clone https://github.com/Arnoldew/ecommerce-price-analysis.git
cd ecommerce-price-analysis

# Install dependencies
pip install pandas numpy matplotlib seaborn requests beautifulsoup4 jupyter

# (Optional) Re-run the scraper to collect fresh data
python scraper/scraper.py

# Launch the analysis notebook
jupyter notebook notebook/price_analysis.ipynb
```

---

## Author

**Arnoldew Ray Ruby**
- GitHub: [@Arnoldew](https://github.com/Arnoldew)
- LinkedIn: [arnoldew-ray-ruby](https://www.linkedin.com/in/arnoldew-ray-ruby/)

---

*Part of a 10-project data analyst portfolio.*
