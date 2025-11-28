_persona_db_completions() {
    local cur prev opts
    COMPREPLY=()

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    opts="--url -u --help -h"

    # Special handling for URL flags
    case "$prev" in
        --url|-u)
            return 0
            ;;
    esac

    # If current word empty OR starts with "-", show all options
    if [[ -z "$cur" || "$cur" == -* ]]; then
        COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
        return 0
    fi
}

complete -F _persona_db_completions persona_db.py
complete -F _persona_db_completions ./persona_db.py
