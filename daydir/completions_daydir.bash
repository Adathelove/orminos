# completions/driver_daydir-completion.bash

_driver_daydir_completions() {
    local cur prev opts
    COMPREPLY=()

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # All supported commands
    opts="path inspect mkdir init schema --help --usage"

    # If current word begins with "-" show only flags
    if [[ "$cur" == -* ]]; then
        COMPREPLY=( $(compgen -W "--help --usage" -- "$cur") )
        return 0
    fi

    # Otherwise complete subcommands
    COMPREPLY=( $(compgen -W "$opts" -- "$cur") )
    return 0
}

# Register completion for explicit calls:
complete -F _driver_daydir_completions ./driver_daydir.py
complete -F _driver_daydir_completions driver_daydir.py

