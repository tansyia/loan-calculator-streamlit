# ---------- 安全输入函数 ----------
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('❌ 输入格式错误，请输入数字，例如 5 或 12.5')


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('❌ 输入格式错误，请输入整数，例如 3 或 10')


# ---------- 主程序 ----------
print('==============================')
print('📊 贷款余额利息计算器')
print('==============================')
print('以下计算方为计算余额利息 (Interest on balance)\n')

while True:
    LN = get_float('请输入个人贷款额（personal loan）: RM ')
    RT = get_float('请输入年利率（annual interest rate），例如 5 表示 5%: ')

    years = get_int('请输入还款年数（years）: ')
    months = get_int('请输入额外月份（months，若无则填0）: ')
    PD = years * 12 + months
    print(f'还款期总共是 {PD} 个月（约为 {PD / 12:.2f} 年）')

    Inst = get_float('请输入分期付款额（monthly instalment）: RM ')

    early_months = get_int('你想计算还款期前几个月的利息？（若不需要请填0）: ')
    if early_months > 0:
        max_months = min(early_months, PD)
        print(f'将只计算前 {max_months} 个月的利息...\n')
    else:
        max_months = PD
        print(f'将计算完整还款期的利息...\n')

    # ---------- 计算利息 ----------
    balance = LN
    monthly_rate = RT / 100 / 12
    total_interest = 0

    print('--- 每月还款详情 ---')
    for i in range(1, max_months + 1):
        interest = balance * monthly_rate
        principal = Inst - interest
        balance -= principal
        total_interest += interest

        print(f'第 {i} 期: 利息 = RM {interest:.2f}, 本金 = RM {principal:.2f}, 剩余贷款 = RM {balance:.2f}')

        if balance <= 0:
            break

    # ---------- 汇总结果 ----------
    print('\n--- 汇总 ---')
    print(f'共计算 {i} 个月的还款')
    print(f'累计利息: RM {total_interest:.2f}')
    print(f'总还款额: RM {Inst * i:.2f}')

    # ---------- 退出判断 ----------
    taf = input('\n现在退出？(yes or no): ').strip().lower()
    if taf == 'yes':
        print('感谢使用贷款利息计算器！👋')
        break
