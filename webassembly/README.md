

# WASM学习

## 环境安装

### Rust

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

*以上仅限Linux或MacOS，Windows中安装[参考此处](https://forge.rust-lang.org/infra/other-installation-methods.html)。*

验证安装是否成功`rustc --version`

```sh
guogang@guog-mbp ~ % rustc --version
rustc 1.79.0 (129f3b996 2024-06-10)
```

升级rust环境使用`rustup`工具

```sh
rustup update
```

Rustup 会安装 Rust 的编译器 `rustc`、Rust 的包管理工具 `cargo`、Rust 的标准库 `rust-std` 以及一些有用的文档 `rust-docs`。

### wasm-pack

`wasm-pack`把Rust代码编译成 WebAssembly 并制造出正确的 `npm` 包。

安装

```sh
cargo install wasm-pack
```

验证安装

```sh
guogang@guog-mbp ~ % wasm-pack --version
wasm-pack 0.13.1
```

### 安装Node.js和Npm

安装[Node.js](https://nodejs.org/zh-cn)，并[注册Npm账户](https://www.npmjs.com/signup)。

登录npm

```sh
npm adduser
```



## 编码

创建脚手架

```sh
cargo new --lib hello-wasm
```

写代码

## 编译

将代码编译为WebAssembly.

确保cargo.toml文件内容正确

```toml
[package]
name = "hello-wasm"
version = "0.1.0"
authors = ["Your Name <you@example.com>"]
description = "A sample project with wasm-pack"
license = "MIT/Apache-2.0"
repository = "https://github.com/yourgithubusername/hello-wasm"

[lib]
crate-type = ["cdylib"]

[dependencies]
wasm-bindgen = "0.2"
```

注意`[lib]`和`[dependencies]`两部分。

构建包

```sh
wasm-pack build --scope mynpmusername
```

执行完成后，在`pkg`目录下有一个npm包。

## 发布WebAssembly包到Npm

```sh
cd pkg
npm publish --access=public
```

## 常见问题

### Module parse failed: Unknown element type in table: 0xNaN

运行 `nom run start`后出现：

```txt
ERROR in ./pkg/index_bg.wasm
Module parse failed: Unknown element type in table: 0xNaN
```
解决办法,安装最新版`wasm-bindgen`，如下：
```sh
cargo install wasm-bindgen-cli --git "https://github.com/rustwasm/wasm-bindgen"
```
参考: https://github.com/rustwasm/wasm-bindgen/issues/4211#issuecomment-2450852442

## WebAssembly能力

- 数据运算
- canvas绘制
- Dom操作
- Node.JS和Deno
- HTTP请求
