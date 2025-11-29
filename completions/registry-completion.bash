# completions/registry-completion.bash

_registry_completions() {
    local cur prev opts
    COMPREPLY=()

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # All top-level options
    opts="--url -u --today --select --auto --help -h"

    case "$prev" in
        --url|-u)
            # URL arg, no completion suggestions
            return 0
            ;;
    esac

    # If current word is empty or begins with "-", list all options
    if [[ -z "$cur" || "$cur" == -* ]]; then
        COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
        return 0
    fi
}

# Register completion for both invocation forms
complete -F _registry_completions registry.py
complete -F _registry_completions ./registry.py

