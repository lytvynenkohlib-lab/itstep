import warnings
warnings.filterwarnings("ignore", SyntaxWarning)
warnings.filterwarnings("always", ImportWarning)

warnings.warn("warning, no code here",SyntaxWarning)
warnings.warn("warning, module no code here", ImportWarning)