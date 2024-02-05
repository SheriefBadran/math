

# Create the SSH config file with the desired content
cat <<EOT > /home/vscode/.ssh/config
    Host *
    AddKeysToAgent yes
    IdentityFile /home/vscode/.ssh/id_rsa
EOT

# Ensure the config file is properly secured
chmod 600 /home/vscode/.ssh/config

# Execute the original CMD command, if applicable
exec "$@"



