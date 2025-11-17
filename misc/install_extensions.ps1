<<<<<<< HEAD

# VS Code extensions to install
$extensions = @(
    "bierner.emojisense",
    "michaelCurrin.auto-commit-msg",
    "ms-python.black-formatter",
    "github.codespaces",
    "github.vscode-pull-request-github",
    "github.github-vscode-theme",
    "ms-toolsai.jupyter",
    "esbenp.prettier-vscode",
    "ms-python.python",
    "ms-python.debugpy",
    "ericsia.pythonsnippets3",
    "ms-vscode.remote-repositories",
    "emmanuelbeziat.vscode-great-icons",
    "ms-vscode.powershell",
    "formulahendry.code-runner"
)
foreach ($extension in $extensions) {
    code --install-extension $extension
}
=======

# VS Code extensions to install
$extensions = @(
    "bierner.emojisense",
    "michaelCurrin.auto-commit-msg",
    "ms-python.black-formatter",
    "github.codespaces",
    "github.vscode-pull-request-github",
    "github.github-vscode-theme",
    "ms-toolsai.jupyter",
    "esbenp.prettier-vscode",
    "ms-python.python",
    "ms-python.debugpy",
    "ericsia.pythonsnippets3",
    "ms-vscode.remote-repositories",
    "emmanuelbeziat.vscode-great-icons",
    "ms-vscode.powershell",
    "formulahendry.code-runner"
)
foreach ($extension in $extensions) {
    code --install-extension $extension
}
>>>>>>> 071ea7f10dd3616d394fdce02072ea5f94b2082f
