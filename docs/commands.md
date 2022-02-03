# Command list

|                                                                                                                                               |                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `tncli start [-h] [--name NAME] {wallet}`                                                                                                     | Create simple project, currently only wallet available, name parameter is the name of created folder                                                                                                          |
| `tncli deploy [-h] [--net {testnet,mainnet}] [--workchain WORKCHAIN] [--ton TON] [--update]`                                                  | Deploy contract to blockchain, will create StateInit and external message, create boc and send it to blockchain, ton parameter - how much currency need to send, update - update local cached network configs |
| `tncli build`                                                                                                                                 | Same as `tncli func build`, build project's files in `func/` to  `build/`                                                                                                                                     |
|                                                                                                                                               |                                                                                                                                                                                                               |
| `tncli fift [-h] [--net {testnet,mainnet}] [--workchain WORKCHAIN] [--update] [--fift-args FIFT_ARGS]  [--lite-client-args LITE_CLIENT_ARGS]` |                                                                                                                                                                                                               |
| `tncli fift run [files] [command lite arguments to files]`                                                                                    | Run fift file                                                                                                                                                                                                 |
| `tncli fift interactive`                                                                                                                      | Run fift interactive shell a.k.a. default method                                                                                                                                                              |
| `tncli fift sendboc [files] [command lite arguments to files]`                                                                                | Run fift file and send boc to blockchain  (you need to specify saveboc and in stack need to be boc)                                                                                                           |
| `tncli f`                                                                                                                                     | You can use f instead of fift                                                                                                                                                                                 |
|                                                                                                                                               |                                                                                                                                                                                                               |
| `tncli lite-client [-h] [--net {testnet,mainnet}] [--update] [--lite-client-args LITE_CLIENT_ARGS]`                                           |                                                                                                                                                                                                               |
| `tncli lite-client interactive`                                                                                                               | Run lite-client interactive shell a.k.a. default method                                                                                                                                                       |
| `tncli lite-client [ANY]`                                                                                                                     | Run all other methods and arguments will be passed to lite-client shell, e.g. tncli lc help                                                                                                                   |
| `tncli lc`                                                                                                                                    | You can use lc instead of lite-client                                                                                                                                                                         |
|                                                                                                                                               |                                                                                                                                                                                                               |
| `tncli func [-h] [--func-args FUNC_ARGS]`                                                                                                     |                                                                                                                                                                                                               |
| `tncli func build`                                                                                                                            | Build project's files in `func/` to `build/`                                                                                                                                                                  |
| `tncli fc`                                                                                                                                    | You can use fc instead of func                                                                                                                                                                                |
|                                                                                                                                               |                                                                                                                                                                                                               |
| `tncli build-cli-lib`                                                                                                                         | Technical command to create cli.fif                                                                                                                                                                           |