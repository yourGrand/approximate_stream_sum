# Approximate Stream Sum

A randomised streaming algorithm that efficiently approximates the sum of elements in a data stream using

O(log(log(m)) + log(n))

space complexity, where m is the stream length and n is the maximum value in the stream.

Please refer to analysis.pdf for a more detailed explanation and proof of the algorithm.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

---

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone git@github.com:yourGrand/approximate_stream_sum.git
    ```

2. Navigate into the project directory:

    ```bash
    cd approximate_stream_sum
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    ```

4. Activate the virtual environment:
    - On Windows:

      ```bash
      .venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source .venv/bin/activate
      ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

To run the script, use the following command:

```bash
python approximate_stream_sum.py
```
