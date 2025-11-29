# completions/registry-completion.bash

_registry_completions() {
    local cur prev opts
    COMPREPLY=()

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    opts="--url -u --today --select --help -h"

    case "$prev" in
        --url|-u)
            # URL arg, no completion
            return 0
            ;;
    esac

    if [[ -z "$cur" || "$cur" == -* ]]; then
        COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
        return 0
    fi
}

# Register completion for both invocation styles
complete -F _registry_completions registry.py
complete -F _registry_completions ./registry.py
