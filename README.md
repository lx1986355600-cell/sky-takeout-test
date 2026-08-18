# 苍穹外卖自动化测试项目

基于苍穹外卖后端系统，独立设计并实施的自动化测试项目。

## 技术栈

- **接口测试**：Python + Pytest + Requests
- **UI自动化**：Selenium WebDriver（PO设计模式）
- **性能测试**：JMeter
- **测试报告**：Allure
- **CI/CD**：GitHub Actions

## 项目结构
```text
sky-takeout-test/
├── .github/workflows/
│   └── test.yml           # GitHub Actions CI/CD 流水线配置文件
├── pages/
│   └── login_page.py      # PO模式页面层：统一管理UI元素定位和操作逻辑
├── test_login.py          # 接口自动化：登录模块（含参数化与异常边界测试）
├── test_dish.py           # 接口自动化：菜品模块（含Token提取与鉴权验证）
├── test_ui_login.py       # UI自动化：基于Web端的登录页面交互测试
├── conftest.py            # Pytest核心配置：全局Fixture与Token依赖注入
├── performance_test.jmx   # JMeter 性能压测脚本
└── README.md              # 项目说明文档
```

## 测试覆盖

### 接口测试
| 模块 | 用例数 | 覆盖场景 |
|------|--------|---------|
| 登录接口 | 7条 | 正常登录、密码错误、账号不存在、参数化边界测试 |
| 菜品接口 | 3条 | 正常查询、分页查询、未登录鉴权验证 |

### UI自动化测试
| 模块 | 用例数 | 覆盖场景 |
|------|--------|---------|
| 登录页面 | 2条 | 正常登录跳转验证、错误密码提示验证 |

### 性能测试
- 对"查询菜品列表"接口进行100并发压测
- 平均响应时间：25ms，P90：32ms，TPS：10.3/sec，错误率：0%

## 测试亮点

1. **PO设计模式**：页面元素与测试逻辑分离，UI改动只需修改页面层
2. **参数化测试**：使用 `@pytest.mark.parametrize` 实现一个函数覆盖多组数据
3. **显式等待**：使用 `WebDriverWait` 替代 `time.sleep()`，提升脚本稳定性
4. **公共fixture**：conftest.py统一管理登录token，避免重复代码
5. **CI/CD集成**：GitHub Actions在每次push时自动触发测试流程

## 如何运行

### 前置条件
- 启动苍穹外卖后端服务（默认端口8080）
- 启动苍穹外卖前端服务（默认端口80）

### 安装依赖
在项目根目录下打开终端，运行以下命令安装所需的三方库：
```bash
pip install requests pytest allure-pytest selenium
```

### 运行接口测试
执行登录和菜品模块的接口自动化测试用例，并输出详细日志：
```bash
python -m pytest test_login.py test_dish.py -v
```

### 运行 UI 测试
执行 Web 端登录页面的 UI 自动化测试用例：
```bash
python -m pytest test_ui_login.py -v
```

### 生成 Allure 测试报告
首先运行测试用例并收集测试数据到 `allure-results` 目录，然后启动 Allure 服务在浏览器中查看可视化报告：
```bash
python -m pytest test_login.py test_dish.py -v --alluredir=allure-results
allure serve allure-results
```