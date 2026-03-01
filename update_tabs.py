import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update CSS
css_addition = """
/* --- Tab Navigation Styles --- */
.top-tabs-nav {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(30, 138, 154, 0.2);
  display: flex;
  justify-content: center;
  padding: 0 10px;
  overflow-x: auto;
  scrollbar-width: none;
}
.top-tabs-nav::-webkit-scrollbar { display: none; }

.tab-btn {
  background: transparent;
  border: none;
  font-size: 1.1rem;
  font-weight: 600;
  color: #6B7280;
  padding: 15px 20px;
  cursor: pointer;
  position: relative;
  transition: color 0.3s;
  white-space: nowrap;
}
.tab-btn:hover {
  color: var(--cyan-deep);
}
.tab-btn.active {
  color: var(--cyan-deep);
}
.tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 10%;
  width: 80%;
  height: 3px;
  background: var(--cyan-deep);
  border-radius: 3px 3px 0 0;
}

/* --- Tab Content Styles --- */
.tab-pane {
  display: none;
  animation: fadeIn 0.4s ease-in-out;
}
.tab-pane.active {
  display: block;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
"""

if "/* --- Tab Navigation Styles --- */" not in css:
    css = css_addition + "\n" + css
    with open('index.css', 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Update HTML Structure

# Add Top Navigation
nav_html = """
    <!-- 顶部标签导航 -->
    <nav class="top-tabs-nav" id="topNav">
        <button class="tab-btn active" data-target="tab-pricing">选膜套餐</button>
        <button class="tab-btn" data-target="tab-parameters">参数对比</button>
        <button class="tab-btn" data-target="tab-intro">品牌介绍</button>
        <button class="tab-btn" data-target="tab-service">施工售后</button>
    </nav>
"""
html = html.replace('<body>', '<body>\n' + nav_html)

# Add Tab Wrappers
# Tab 1: 选膜套餐 (Pricing)
html = html.replace('<!-- 模块五：全部套餐价格 -->', '<!-- TAB: 选膜套餐 -->\n    <div id="tab-pricing" class="tab-pane active">\n    <!-- 模块九：选膜推荐引导 -->\n    <section class="recommendation">')
html = html.replace('<!-- 模块九：选膜推荐引导 -->\n    <section class="recommendation">', '')
html = re.sub(r'(<section class="recommendation".*?</section>)', '', html, flags=re.DOTALL)
html = html.replace('<!-- 模块五：全部套餐价格 -->', '<!-- 模块五：全部套餐价格 -->\n    <section class="recommendation">\n        <div class="container">\n            <div class="recommendation-banner">\n                <div class="recommend-content quantum-glass">\n                    <h2 style="font-size: 2rem; margin-bottom: 20px;">找准您的专属套膜</h2>\n                    <p style="margin-bottom: 30px; font-size: 1.1rem; color: rgba(255,255,255,0.9);">\n                        不知道怎么选？对号入座，一秒找到适合您的最佳组合。</p>\n\n                    <div style="display: flex; flex-direction: column; gap: 15px;">\n                        <div\n                            style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;">\n                            <div>\n                                <h4 style="color: white; font-size: 1.1rem; margin-bottom: 5px;">🚘 豪华车 / 50万以上</h4>\n                                <span style="font-size: 0.9rem;">推荐：至尊全防护（钻石系满配）</span>\n                            </div>\n                            <strong style="font-size: 1.2rem;">¥9,440</strong>\n                        </div>\n\n                        <div\n                            style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;">\n                            <div>\n                                <h4 style="color: white; font-size: 1.1rem; margin-bottom: 5px;">🚕 中高端 / 30万-50万</h4>\n                                <span style="font-size: 0.9rem;">推荐：至尊豪华（钻石前挡+顶级侧后）</span>\n                            </div>\n                            <strong style="font-size: 1.2rem;">¥5,160</strong>\n                        </div>\n\n                        <div\n                            style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;">\n                            <div>\n                                <h4 style="color: white; font-size: 1.1rem; margin-bottom: 5px;">🚗 家用车 / 15万-30万</h4>\n                                <span style="font-size: 0.9rem;">推荐：至尊经济 或 顶级尊享</span>\n                            </div>\n                            <strong style="font-size: 1.2rem;">¥3,760起</strong>\n                        </div>\n\n                        <div\n                            style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;">\n                            <div>\n                                <h4 style="color: white; font-size: 1.1rem; margin-bottom: 5px;">🚙 经济型 / 15万以内</h4>\n                                <span style="font-size: 0.9rem;">推荐：顶级标准 或 各类半车特惠</span>\n                            </div>\n                            <strong style="font-size: 1.2rem;">¥2,340起</strong>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </section>\n\n    <!-- 模块五：全部套餐价格 -->')

# Set tab end for pricing before parameters
html = html.replace('<!-- 模块六：全部产品参数 -->', '    </div>\n\n    <!-- TAB: 参数对比 -->\n    <div id="tab-parameters" class="tab-pane">\n    <!-- 模块六：全部产品参数 -->')

# Set tab end for parameters after comparison
html = html.replace('<!-- 模块一：Hero 首屏 -->', '    </div>\n\n    <!-- TAB: 品牌介绍 -->\n    <div id="tab-intro" class="tab-pane">\n    <!-- 模块一：Hero 首屏 -->')

# Set tab end for intro before process
html = html.replace('<!-- 模块四：贴膜施工流程 -->', '    </div>\n\n    <!-- TAB: 施工售后 -->\n    <div id="tab-service" class="tab-pane">\n    <!-- 模块四：贴膜施工流程 -->')

# Remove FAQ and add back inside tab-service
html = re.sub(r'(<!-- 模块八：常见问题 FAQ -->.*?</section>)', '', html, flags=re.DOTALL)
html = html.replace('    <footer>', '    <!-- 模块八：常见问题 FAQ -->\n    <section class="faq" id="faq">\n        <div class="container">\n            <div class="section-header">\n                <h2>常见问题 FAQ</h2>\n                <p>消除您的疑虑，明明白白选好膜</p>\n            </div>\n\n            <div class="faq-grid quantum-glass" style="padding: 40px;">\n                <div class="faq-item">\n                    <h3><span class="faq-icon">Q：</span>金属膜会影响手机信号和车载导航吗？</h3>\n                    <p>完全不会。量子膜采用航天级磁控溅射工艺，使用黄金、银、钛等贵重金属。现代5G频段的电磁波可从金属原子间隙自然穿透，地下车库或偏远山区均实测对信号毫无干扰。</p>\n                </div>\n                <div class="faq-item">\n                    <h3><span class="faq-icon">Q：</span>前挡为什么只能选70或80系列？</h3>\n                    <p>国家法规强制要求，汽车前挡风玻璃及驾驶员视区透光率须达到70%以上，以保障雨夜行车视线安全。70/80系列即代表透光率≥70%，我们在合规前提下将隔热能力做到了极致。</p>\n                </div>\n                <div class="faq-item">\n                    <h3><span class="faq-icon">Q：</span>钻石系列和水晶系列怎么选？</h3>\n                    <p>钻石（至尊）：追求终极体验首选，10层金属，3mil双倍防爆厚度，隔热最顶。水晶（顶级）：性价比玩家首选，2mil标准厚度，拥有高达78%透光率的陶瓷透亮清晰视野。</p>\n                </div>\n                <div class="faq-item">\n                    <h3><span class="faq-icon">Q：</span>10年质保具体"保"的是什么？</h3>\n                    <p>覆盖因膜质量问题引发的：起泡脱层、开胶脱落、自发断裂、胶水聚集成团、视线发黄发彩等。钻石系列更提供业内独享保障：10年内如果用仪器测定您的隔热效果下降超过1%，免费重贴。</p>\n                </div>\n                <div class="faq-item">\n                    <h3><span class="faq-icon">Q：</span>前后排（侧后挡）选30还是15透光率？</h3>\n                    <p>透光30%：视野更开阔，夜晚倒车看后视镜更清晰。透光15%：私密性更好（外面看不清里面），隔热更强。最流行做法：前门贴30保安全，后门后窗贴15重防晒和隐私。</p>\n                </div>\n                <div class="faq-item">\n                    <h3><span class="faq-icon">Q：</span>为什么强调要去官方授权中心？</h3>\n                    <p>好膜三分靠纸，七分靠贴。钻石系膜比普通膜厚一倍多且金属层娇贵，普通店手工切割、烤枪火候不对极易烤焦或留下卷边气泡。CHCC广州壕马乃官方运营中心，特聘高阶认证技师，配备无尘车间微水施工。</p>\n                </div>\n            </div>\n        </div>\n    </section>\n    </div>\n\n    <footer>')


# Change hero buttons to switch tabs
html = html.replace('href="#pricing" class="btn btn-primary"', 'href="#" class="btn btn-primary js-switch-tab" data-target="tab-pricing"')
html = html.replace('href="#parameters" class="btn btn-primary"', 'href="#" class="btn btn-primary js-switch-tab" data-target="tab-parameters"')


js_html = """
    <!-- Tab Switching Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const tabBtns = document.querySelectorAll('.tab-btn');
            const tabPanes = document.querySelectorAll('.tab-pane');
            const jsSwitchBtns = document.querySelectorAll('.js-switch-tab');

            function switchTab(targetId) {
                // Remove active class from all
                tabBtns.forEach(btn => btn.classList.remove('active'));
                tabPanes.forEach(pane => pane.classList.remove('active'));

                // Add active class to target
                const targetBtn = document.querySelector(`.tab-btn[data-target="${targetId}"]`);
                const targetPane = document.getElementById(targetId);
                
                if (targetBtn) targetBtn.classList.add('active');
                if (targetPane) targetPane.classList.add('active');
                
                // Scroll to top of nav
                const navElement = document.getElementById('topNav');
                if (navElement) {
                   window.scrollTo({
                       top: navElement.offsetTop,
                       behavior: 'smooth'
                   });
                }
            }

            // Bind top nav clicks
            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    switchTab(btn.dataset.target);
                });
            });

            // Bind cross-tab links (e.g. hero buttons)
            jsSwitchBtns.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    switchTab(btn.dataset.target);
                });
            });
        });
    </script>
"""

if "<!-- Tab Switching Logic -->" not in html:
    html = html.replace('</body>', js_html + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

