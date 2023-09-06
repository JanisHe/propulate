# Contributing to Propulate

Welcome to ``Propulate``! We're thrilled that you're interested in contributing to our open-source project. 
By participating, you can help improve the project and make it even better. 

## How to Contribute

1. **Fork the Repository**: Click the "Fork" button at the top right corner of this repository's page to create your own copy.

2. **Clone Your Fork**: Clone your forked repository to your local machine using Git:
   ```bash
   git clone https://github.com/Helmholtz-AI-Energy/propulate.git
   ```

3. **Create a Branch**: Create a new branch for your contribution. Choose a descriptive name:
   ```bash
   git checkout -b your-feature-name
   ```

4. **Make Changes**: Make your desired changes to the codebase. Please stick to the following guidelines: 
   * ``Propulate`` uses black code styling and so should you if you would like to contribute.
   * Use American English for all comments and docstrings in the code.
   * Please use the [NumPy Docstring Standard](https://numpydoc.readthedocs.io/en/latest/format.html) for your docstrings:
      
     ```python
     """
     Short Description

     Long Description (if needed)

     Parameters
     ----------
     param1 : type
     Description of param1.

     param2 : type, optional
     Description of param2. (if it's an optional argument)

     Returns
     -------
     return_type
         Description of the return value.

     Other Parameters
     ----------------
     param3 : type
         Description of param3. (if there are additional parameters)

     Raises
     ------
     ExceptionType
         Description of when and why this exception might be raised.

     See Also
     --------
     other_function : Related function or module.

     Examples
     --------
        >>> import numpy as np
        >>> x = np.array([1, 2, 3])
        >>> y = np.square(x)
        >>> print(y)
     array([1, 4, 9])

     Notes
     -----
     Additional notes, recommendations, or important information.
     """
        
5. **Commit Changes**: Commit your changes with a clear and concise commit message:
   ```bash
   git commit -m "Add your commit message here"
   ```

6. **Push Changes**: Push your changes to your fork on GitHub:
   ```bash
   git push origin your-feature-name
   ```

7. **Open a Pull Request**: Go to the [original repository](https://github.com/Helmholtz-AI-Energy/propulate.git) and click the "New Pull Request" button. Follow the guidelines in the template to submit your pull request.

## Code of Conduct

Please note that we have a [Code of Conduct](CODE_OF_CONDUCT.md), and we expect all contributors to follow it. Be kind and respectful to one another.

## Questions or Issues

If you have questions or encounter any issues, please create an issue in the [Issues](https://github.com/Helmholtz-AI-Energy/propulate/issues) section of this repository.

Thank you for your contribution!