#encoding: utf-8
import os, csv, sys
from bk_functions import *
from bk_functions import __

# trait class from BKClasses.py, modified
class Trait:
    """This class is for traits (skills with special effects that are either on or off)."""
    # eff1, eff2, eff3 are kept for backwards compatibility, until I clean up the code
    def __init__(self, name, verb = "be", eff1 = None, eff2 = None, eff3 = None, effects = None, opposite = None, archetype = None, base_description = "", public=True):
        # Setting 'public' to True means any girl can generate with this trait. False means it can only be generated through code or _BK.ini
        self.name = name
        self.verb = verb
        self.effects = []
        if effects:
            self.effects = make_list(effects, Effect)
        if eff1:
            self.effects.append(eff1)
        if eff2:
            self.effects.append(eff2)
        if eff3:
            self.effects.append(eff3)

        if opposite == None:
            self.opposite = []
        else:
            self.opposite = make_list(opposite)
        self.archetype = archetype
        self.base_description = base_description
        self.public = public
    
    def to_list(self):
        ret = [self.name, self.base_description]
        for ef in self.effects:
            ret.append(','.join([ef.type, ef.target]))
            ret.append(ef.value)
        return ret
        
class Effect():
    """This class is used for all effects applying to a character"""
    def __init__(self, type, target = None, value = 0, chance = 1.0, scales_with = None, scope = None, dice=False, change_cap=True, duration=-1, source=None):
        self.type = type
        self.target = target
        self.value = value
        self.chance = chance
        self.scales_with = scales_with
        self.scope = scope
        self.source = source
        self.dice = dice
        self.change_cap = change_cap
        self.duration = duration # -1 duration = infinite. Duration is only used for buff effects
        
    def __repr__(self):
        line = f"{{{self.type}; {self.target}; {self.value};"
        if self.chance != 1.0:
            line += f"chance={self.chance}; "
        if self.scales_with:
            line += f"scales_with={self.scales_with}; "
        if self.scope:
            line += f"scope={self.scope}; "
        if self.dice:
            line += f"dice=True; "
        if self.change_cap:
            line += "change_cap=True; "
        if self.duration >= 0:
            line += f"duration={self.duration}; "
        if self.source:
            line += f"source={self.source}"
        line += "}"
        return line
    
    def get_description(self):
        val = self.value
        target = self.target
        text1 = ""

        if self.type in ("special", "personality"):

            if target == "naked":
                text1 = "十分乐意裸体"

            elif target == "level":
                text1 = "+1等级 (最高等级: " + str(val) + ")"

            elif target == "advertising power":
                text1 = "提高广告的效果 (提高青楼的声望增速,客流量和顾客的预算)。"

            elif target == "heal minion":
                text1 = "治疗一个受伤的单位。"

            elif target == "workwhore":
                text1 = "她可以一边正常的工作，一边勾引客人上床。"

            elif target == "lucky":
                text1 = "工作或卖淫时提高判定大成功的概率 (效果无法叠加)"

            elif target == "unlucky":
                text1 = "工作或卖淫时提高判定大失败的概率"

            elif target == "temptress":
                text1 = "能说服不情愿的顾客接受另一种性行为"

            elif target == "pickpocket":
                text1 = "有机会从顾客那里偷取额外10%的小费，如果被抓住会降低声望"

            elif target == "random item":
                text1 = "顾客小概率“遗漏”随机物品"

            elif target == "BBCR bonus":
                text1 = "如果她的外貌、身材、魅力或优雅等级足够高，可能会提高客户的满意度"

            elif target == "LOCS bonus":
                text1 = "如果她的性欲，服从，体质或敏感等级足够高，可能会提高客户的满意度"

            elif target == "whore mood modifier":
                text1 = "卖淫时她的情绪会升高"

            elif target == "job prestige":
                text1 = "可以在普通工作中获得声望"

            elif target == "skill catch up":
                text1 += "每天晚上，她会帮助其他属性比她低的女孩获得永久的属性提升 (每升一阶多帮助一人)"

            elif target == "effect chance":
                text1 += "使天赋生效的基础几率加倍 (最多50%)"

            elif target == "defender":
                text1 += "即使你没有行动力了你也可以保护她们"

            elif target == "snake eyes":
                text1 += "催眠永远不会失败"

            elif target == "safe":
                text1 += "青楼的发生紧急事件时至少保留 " + str(val) + " 金币。"

            elif target == "focus":
                text1 += "如果女孩专精于一种性行为，+25%小费和声望收益 (不包括双飞和群交行为)"

            elif target == "rest shield":
                text1 += "休息时，她可以对自己或朋友施放一层魔法护盾，保护其免受攻击"

            elif target == "ignore budgets":
                text1 += "无视顾客的预算限制"

            elif target == "ignore energy":
                text1 += "每次互动都有概率无视精力损耗"

            text1 = "在作为妓女工作时接受群交行为" if target == "group" else text1
            text1 = "在作为妓女工作时接受双飞行为" if target == "bisexual" else text1
            text1 = "在任何时候包括平时都保持裸体" if target == "naked" else text1
            text1 = "在作为妓女工作时接受激烈的多人群交" if target == "orgy" else text1
            text1 = "在作为妓女工作时戴上装饰扮演兽耳娘" if target == "ponygirl" else text1

            return __(text1)

        elif self.type == "instant" and target == "heal":
            return "疗伤时间减少 " + str(val) + "天。"

        if self.type == "set":
            target = "所有技能上限值" if target == "all skill max" else target
            text1 += "改变" + target + __("到") + str(val)
            if self.scope:
                text1 += " (%s)" % tl_cn(self.scope, misc_name_dict)
            return text1

        if self.type == "allow":
            if target.endswith("preference"):
                target = "享受服务倾向" if target == "waitress preference" else target
                target = "观看舞蹈倾向" if target == "dancer preference" else target
                target = "接受按摩倾向" if target == "masseuse preference" else target
                target = "观摩表演倾向" if target == "geisha preference" else target
                target = "侍奉倾向" if target == "service preference" else target
                target = "性交倾向" if target == "sex preference" else target
                target = "肛交倾向" if target == "anal preference" else target
                target = "调教倾向" if target == "fetish preference" else target
                target = "群交倾向" if target == "group preference" else target
                target = "双飞倾向" if target == "bisexual preference" else target
                target = "所有性行为倾向" if target == "all sex acts preference" else target
                text1 += "允许您增加客人的' " + target + " 最多 +" + str(50*val) + "%。"
            else:
                text1 += "现在" + tl_cn(target, misc_name_dict) + "也会光顾你的青楼了。"

            return text1

        if 0.75 <= self.chance < 1.0:
            text1 += "极高概率"

        elif 0.25 < self.chance < 0.75:
            text1 += "高概率"
        elif self.chance <= 0.25:
            text1 += "小概率"


        if self.type == "reroll":
            if text1:
                text1 += "再掷一次... "
            else:
                text1 += __("reroll")

            if self.target == "job critical failure":
                text1 += __(" a critical failure when working")

            return text1

        if self.dice:
            text1 += "1-"

        elif is_string(val):
            pass

        elif val > 0:
            text1 += "+"

        if self.type in ("gain", "instant"): # Permanent x gain (xp, reputation...)
            try:
                text1 += __(str(round_int(val))) + " "
            except:
                text1 += __(str(val)) + " "

            if self.target.endswith("preference") or self.target.endswith("preferences"):
                text1 += __(" to ")

        elif self.type == "change": # Temporary x effect (can be added or removed)
            # text1 += str(round_best(val, 2)) + __("到")
            text1 += str(round_best(val, 2))
            if target.endswith("training obedience target"):
                target = "作为训练时所需服从"
            if target.endswith("train obedience target"):
                target = "作为训练时所需服从"
            if target.endswith("work obedience target"):
                target = "作为工作时所需服从"
            if target.endswith("fight challenges"):
                target = "挑战中战斗加成"

        elif self.type == "resist":
            text1 += str(round_int(val)) + __(" negated {#1}")

        elif self.type == "spillover":
            percentage = round_int(val * 100)
            self.target = "经验" if self.target == "xp" else self.target
            self.target = "职业经验" if self.target == "jp" else self.target
            text1 += "每当获得" + self.target + "时，其他女孩也收获"+str(percentage) + "%"
            # text1 += str(percentage) + "% " + target + __(" 赚钱的时候分给其他女孩 ")

        elif self.type == "boost": # Temporary % effect (can be removed)

            percentage = round_int(val * 100)

            text1 += str(percentage) + __("% to ")

        elif self.type == "gift":
            text1 += str(round_int(val)) + " "

        elif self.type == "increase satisfaction":
            text1 += str(round_int(val)) + __(" to customer satisfaction for ")

        if self.scope and not target.startswith(self.scope): # The second part handles the 'brothel rep' special case, although renaming brothel reputation to something different to avoid confusion with girl reputation would be a good long-term fix
            #text1 += __(self.scope) + " "
            # text1 += __("{0} {1}").format(__(self.scope), __(target))
            scopexxx = ""
            if self.scope== "brothel":
                scopexxx = "全青楼的"
            elif self.scope == "city":
                scopexxx = "在城市中"
            else:
                scopexxx = __("{0} {1}").format(__(self.scope), __(target))
            text1 += scopexxx + ""
        # else:
        #     text1 += __(target)
        if target in ("rep", "reputation"):
            target="人气"

        ###替换掉中文注释造成的取值错误 strength,charisma,spirit,speed,"Charm","Beauty","Body","Refinement","Sensitivity","Libido","Constitution","Obedience","Service","Sex","Anal","Fetish"
        if target == "body":
            target = "身材"
        if target == "charisma":
            target = "玩家魅力"
        if target == "charm":
            target = "魅力"
        if target == "spirit":
            target = "玩家精神"
        if target == "strength":
            target = "玩家力量"
        if target == "speed":
            target = "玩家速度"
        if target == "beauty":
            target = "美貌"
        if target == "refinement":
            target = "优雅"
        if target == "sensitivity":
            target = "敏感"
        if target == "constitution":
            target = "体格"
        if target == "libido":
            target = "性欲"
        if target == "obedience":
            target = "服从"
        #替换extended_sex_acts = ["naked", "service", "sex", "anal", "fetish", "bisexual", "group"]
        if target == "naked":
            target = "露出"
        if target == "service":
            target = "侍奉"
        if target == "sex":
            target = "性交"
        if target == "anal":
            target = "肛交"
        if target == "fetish":
            target = "调教"
        if target == "bisexual":
            target = "双飞"
        if target == "group":
            target = "群交"
        if target == "all jobs":
            target = "所有工作"
        if target == "all sex acts":
            target = "所有性行为"
        if target == "fear":
            target = "恐惧值"
        if target == "love":
            target = "好感度"
        if target == "waitress":
            target = "女服务员"
        if target == "dancer":
            target = "脱衣舞娘"
        if target == "masseuse":
            target = "按摩技师"
        if target == "geisha":
            target = "表演艺伎"
        target = "脱衣舞娘职业经验收益" if target == "dancer jp gains" else target
        target = "按摩技师职业经验收益" if target == "masseuse jp gains" else target
        target = "女服务员职业经验收益" if target == "waitress jp gains" else target
        target = "表演艺伎职业经验收益" if target == "geisha jp gains" else target
        target = "肛交职业经验收益" if target == "anal jp gains" else target
        target = "性交职业经验收益" if target == "sex jp gains" else target
        target = "侍奉职业经验收益" if target == "service jp gains" else target
        target = "调教职业经验收益" if target == "fetish jp gains" else target
        target = "舞娘职业经验收益" if target == "dancer jp gains" else target
        target = "脱衣舞娘技能收益" if target == "dancer gains" else target
        target = "按摩技师技能收益" if target == "masseuse gains" else target
        target = "女服务员技能收益" if target == "waitress gains" else target
        target = "表演艺伎技能收益" if target == "geisha gains" else target
        target = "肛交技能收益" if target == "anal gains" else target
        target = "性交技能收益" if target == "sex gains" else target
        target = "侍奉技能收益" if target == "service gains" else target
        target = "调教技能收益" if target == "fetish gains" else target
        target = "经验收益" if target == "xp gains" else target
        target = "最大精力" if target == "max energy" else target
        target = "收入" if target == "income" else target
        ###替换 strength,charisma,spirit,speed,"Charm","Beauty","Body","Body","Sensitivity","Libido","Constitution","Obedience","Service","Sex","Anal","Fetish"
        target = "魅力收益" if target == "charm gains" else target
        target = "美貌收益" if target == "beauty gains" else target
        target = "身材收益" if target == "body gains" else target
        target = "敏感收益" if target == "sensitivity gains" else target
        target = "性欲收益" if target == "libido gains" else target
        target = "体格收益" if target == "constitution gains" else target
        target = "服从收益" if target == "obedience gains" else target
        target = "优雅收益" if target == "refinement gains" else target
        target = "所有技能收益" if target == "all skill gains" else target
        target = "所有职业经验收益" if target == "all jp gains" else target

        target = "露出倾向增加" if target == "naked preference increase" else target
        target = "肛交倾向增加" if target == "anal preference increase" else target
        target = "性交倾向增加" if target == "sex preference increase" else target
        target = "侍奉倾向增加" if target == "service preference increase" else target
        target = "调教倾向增加" if target == "fetish preference increase" else target
        target = "群交倾向增加" if target == "group preference increase" else target
        target = "双飞倾向增加" if target == "bisexual preference increase" else target
        target = "所有性行为倾向增加" if target == "all sex acts preference increase" else target

        target = "舞娘职业经验得分" if target == "dancer jp bonus" else target
        target = "按摩师职业经验得分" if target == "masseuse jp bonus" else target
        target = "服务员职业经验得分" if target == "waitress jp bonus" else target
        target = "艺伎职业经验得分" if target == "geisha jp bonus" else target
        target = "肛交职业经验得分" if target == "anal jp bonus" else target
        target = "性交职业经验得分" if target == "sex jp bonus" else target
        target = "侍奉职业经验得分" if target == "service jp bonus" else target
        target = "调教职业经验得分" if target == "fetish jp bonus" else target
        target = "舞娘职业经验" if target == "dancer jp" else target
        target = "按摩师职业经验" if target == "masseuse jp" else target
        target = "服务员职业经验" if target == "waitress jp" else target
        target = "艺伎职业经验" if target == "geisha jp" else target
        target = "肛交职业经验" if target == "anal jp" else target
        target = "性交职业经验" if target == "sex jp" else target
        target = "侍奉职业经验" if target == "service jp" else target
        target = "调教职业经验" if target == "fetish jp" else target
        target = "舞娘结果评价" if target == "dancer results" else target
        target = "按摩师结果评价" if target == "masseuse results" else target
        target = "服务员结果评价" if target == "waitress results" else target
        target = "艺伎结果评价" if target == "geisha results" else target
        target = "肛交结果评价" if target == "anal results" else target
        target = "性交结果评价" if target == "sex results" else target
        target = "侍奉结果评价" if target == "service results" else target
        target = "调教结果评价" if target == "fetish results" else target

        target = "处女时获得的小费" if target == "virgin rep" else target
        target = "处女时获得的人气" if target == "virgin tip" else target
        target = "每天第一位客人的满意度" if target == "first customer satisfaction" else target
        target = "完美结果时获得的小费" if target == "perfect result tip" else target
        target = "完美结果时获得的经验" if target == "perfect result xp" else target
        target = "完美结果时获得的职业经验" if target == "perfect result jp" else target
        target = "每天第一位客人打赏的小费" if target == "first customer tip" else target
        target = "每天第一位客人给予的评价" if target == "first customer rep" else target
        target = "小费" if target == "tip" else target
        target = "所有技能上限值" if target == "all skill max" else target
        target = "所有技能属性" if target == "all skills" else target
        target = "外派任务效果" if target == "quest results" else target
        target = "外派培训效果" if target == "class results" else target
        target = "治疗效果" if target == "heal" else target
        target = "爱情得分" if target == "love bonus" else target
        target = "恐惧得分" if target == "fear bonus" else target
        target = "沉迷性行为" if target == "positive fixation" else target
        target = "保安效果" if target == "security" else target
        target = "保洁效果" if target == "maintenance" else target
        target = "情绪收益" if target == "mood gains" else target
        target = "好感收益" if target == "love gains" else target
        target = "情绪" if target == "mood" else target
        target = "宣传效果" if target == "advertising" else target
        target = "客人数量" if target == "customers" else target
        target = "普通工作时接客人数" if target == "job customer capacity" else target
        target = "个人防御" if target == "defense" else target
        target = "作为妓女时接客人数" if target == "whore customer capacity" else target
        target = "作为训练时所需服从" if target == "train obedience target" else target
        target = "作为工作时所需服从" if target == "job obedience target" else target
        target = "作为妓女时所需服从" if target == "whore obedience target" else target
        target = "精力消耗" if target == "tiredness" else target
        target = "精力消耗" if target == "energy use" else target
        target = "满足保养费时的效用" if target == "positive upkeep modifier" else target
        target = "怪物经验" if target == "monster xp" else target
        target = "野兽经验" if target == "beast xp" else target
        target = "机器经验" if target == "machine xp" else target
        target = "种马经验" if target == "stallion xp" else target
        target = "精力恢复" if target == "energy" else target
        target = "经验" if target == "xp" else target
        target = "属性点" if target == "skill points" else target
        target = "玩家声望" if target == "prestige" else target
        target = "天赋点" if target == "perk" else target
        target = "结交新朋友" if target == "making friends" else target
        target = "来自友谊而获得的心情收益" if target == "mood gains from friendship" else target
        target = "所有性行为偏好" if target == "all sexual preferences" else target
        target = "所有性行为技能" if target == "all sex skills" else target
        target = "性行为激活要求" if target == "sex act requirements" else target
        target = "所有常规技能" if target == "all main skills" else target
        target = "多给保养费的情绪增益影响" if target == "positive upkeep mood modifier" else target
        target = "少给保养费的情绪减益影响" if target == "negative upkeep mood modifier" else target
        target = "只工作半天时精力回复量" if target == "half-shift resting bonus" else target
        target = "接客时客人因难以满足的扣分" if target == "customer penalties" else target
        target = "裸体进行常规工作时获得的小费" if target == "naked bonus" else target
        target = "接受工作或训练的可能性" if target == "obedience tests" else target
        target = "所有常规技能收益" if target == "all regular skills gains" else target
        target = "所有性行为技能收益" if target == "all sex skills gains" else target
        target = "青楼内污垢" if target == "dirt" else target
        target = "催眠效果" if target == "hypnosis result" else target
        target = "魔法值上限" if target == "mana" else target
        target = "农场偏好增加" if target == "farm preference increase" else target
        # target = "作为工作时所需服从" if target == "work obedience target" else target
        # target = "挑战中战斗加成" if target == "fight challenges" else target
        target = "购买价格" if target == "buy" else target
        target = "卖出价格" if target == "sell" else target

        target = "恐惧收益" if target == "fear gains" else target

        target = "总保养费用" if target == "total upkeep" else target
        target = "配饰增幅" if target == "accessory" else target
        target = "项链增幅" if target == "necklace" else target
        target = "戒指增幅" if target == "ring" else target

        target = "保养费" if target == "upkeep" else target
        target = "受伤损失" if target == "hurt" else target
        target = "人气收益" if target == "reputation gains" else target
        target = "卖淫收益" if target == "aconstitution gains" else target
        target = "舞娘职业经验收益" if target == "dancer jp gains" else target
        target = "舞娘职业经验收益" if target == "dancer jp gains" else target

        target = "名声" if target == "brothel reputation" else target
        target = "小费总额" if target == "total tip" else target
        target = "双飞概率" if target == "bisexual chance" else target
        target = "群交概率" if target == "group chance" else target
        target = "作为工作时客户的预算" if target == "job customer budget" else target
        target = "作为妓女时客户的预算" if target == "whore customer budget" else target
        target = "客户活动 " if target == "customer events" else target
        target = "疯狂" if target == "crazy" else target
        target = "服务员倾向" if target == "waitress preference" else target
        target = "舞娘倾向" if target == "dancer preference" else target
        target = "按摩师倾向" if target == "masseuse preference" else target
        target = "艺妓倾向" if target == "geisha preference" else target
        target = "侍奉倾向" if target == "service preference" else target
        target = "性交倾向" if target == "sex preference" else target
        target = "肛交倾向" if target == "anal preference" else target
        target = "调教倾向" if target == "fetish preference" else target
        target = "群交倾向" if target == "group preference" else target
        target = "双飞倾向" if target == "bisexual preference" else target
        target = "所有性行为倾向" if target == "all sex acts preference" else target
        target = "满意度" if target == "satisfaction" else target
        target = "每日爱情" if target == "love per day" else target
        target = "每日恐惧" if target == "fear per day" else target
        target = "丧失理智" if target == "sanity loss" else target
        target = "魔力消耗" if target == "mojo cost" else target
        target = "" if target == "" else target

        text1 += target

        if target == "hurt":
            text1 += __(" damage{#1}")
        elif target in extended_sex_acts:
            text1 += __(" acts{#1}")
        elif target == "random item":
            text1 += "在工作时"

        if self.scales_with:

            if self.scales_with == "equipped":
                text1 += __(" for each equipped item")

            elif self.scales_with == "cust nb":
                text1 += __(" for each customer")
            elif self.scales_with == "job cust nb":
                text1 += __(" for each customer when working")
            elif self.scales_with == "whore cust nb":
                text1 += __(" for each customer when whoring")

            else:
                # text1 += __("对于每点的") + __(self.scales_with)

                if self.scales_with == "strength":
                    scalesxxx="（随主角力量递增）"
                elif self.scales_with == "spirit":
                    scalesxxx="（随主角精神递增）"
                elif self.scales_with == "charisma":
                    scalesxxx="（随主角魅力递增）"
                elif self.scales_with == "speed":
                    scalesxxx="（随主角速度递增）"
                elif self.scales_with == "charisma":
                    scalesxxx="（随主角魅力递增）"
                elif self.scales_with == "defense":
                    scalesxxx="（随个人防御递增）"
                elif self.scales_with in ("rep", "reputation"):
                    scalesxxx="（随个人名声递增）"
                elif self.scales_with == "rank":
                    scalesxxx="（随阶级递增）"
                elif self.scales_with == "equipped": # Counts every piece of equipment
                    scalesxxx="（随装备数递增）"
                elif self.scales_with == "district":
                    scalesxxx="（随地区递增）"
                else:
                    scalesxxx=self.scales_with
                text1 += scalesxxx


        if self.duration > 0:
            text1 += " (持续时间: "

            if self.duration > 1:
                text1 += str(self.duration) + " 次 - 效果不可叠加)"

            elif self.duration == 1:
                text1 += "1次 - 效果不可叠加)"

        return __(text1)


gold_traits = [
    Trait("Naughty", verb="be", eff1 = Effect("boost", "tip", 0.1), eff2 = Effect("personality", "pervert"), archetype="The Slut"),
    Trait("Fascinating", verb="be", eff1 = Effect("change", "job customer capacity", 2), archetype="The Courtesan"),
    Trait("Lust", verb="have", eff1=Effect("change", "whore customer capacity", 1), archetype="The Slut"),
    Trait("Warrior", verb="be a", eff1=Effect("change", "defense", 3), eff2=Effect("personality", "rebel"), archetype="The Bride"),
    Trait("Skilled tongue", verb="have a", eff1=Effect("increase satisfaction", "service", 1), eff2=Effect("increase satisfaction", "bisexual", 1), archetype="The Fox"),
    Trait("Always wet", verb="be", eff1=Effect("increase satisfaction", "sex", 1), eff2=Effect("increase satisfaction", "group", 1), archetype="The Escort"),
    Trait("Tight ass", verb="have a", eff1=Effect("increase satisfaction", "anal", 1), eff2=Effect("increase satisfaction", "fetish", 1), archetype="The Maid"),
    Trait("Playful", verb="be", eff1=Effect("boost", "service preference increase", 0.15), eff2=Effect("boost", "bisexual preference increase", 0.15), eff3=Effect("change", "service max", 10, scales_with = "rank"), archetype="The Player"),
    Trait("Wild", verb="be", eff1=Effect("boost", "sex preference increase", 0.15), eff2=Effect("boost", "group preference increase", 0.15), eff3=Effect("change", "sex max", 10, scales_with = "rank"), archetype="The Slut"),
    Trait("Firm buttocks", verb="have", effects=[Effect("boost", "anal preference increase", 0.1), Effect("change", "anal max", 5, scales_with = "rank")], archetype="The Model"),
    Trait("Dirty mind", verb="be", effects=[Effect("boost", "fetish preference increase", 0.1), Effect("change", "fetish max", 5, scales_with = "rank")], archetype="The Slut"),
    Trait("Magnetic", verb="be", eff1=Effect("boost", "income", 0.02), archetype="The Model"),
    Trait("Loose", verb="be", eff1=Effect("change", "train obedience target", -25), eff2=Effect("boost", "all sex acts preference increase", 0.1), archetype="The Player"),
    Trait("Dedicated", verb="be", eff1=Effect("change", "job obedience target", -25), eff2=Effect("boost", "all jp gains", 0.05), archetype="The Maid"),
    Trait("Provocative", verb="be", eff1=Effect("boost", "dress", 0.5), eff2=Effect("gain", "positive fixation", "cosplay"), archetype="The Model"),
    Trait("Fashionista", verb="be", eff1=Effect("boost", "accessory", 0.25), eff2=Effect("boost", "necklace", 0.25), eff3=Effect("boost", "ring", 0.25), archetype="The Fox"),
    Trait("Perfectionist", verb="be a", eff1=Effect("increase satisfaction", "all jobs", 1), archetype="The Courtesan"),
    Trait("Elite", verb="be", eff1=Effect("special", "ignore budgets", 1), archetype="The Courtesan"),
    Trait("Gifted", verb="be", eff1=Effect("increase satisfaction", "all sex acts", 1), archetype="The Bride"),
    Trait("Fast learner", verb="be a", eff1=Effect("boost", "xp gains", 0.05), eff2=Effect("boost", "all jp gains", 0.05), archetype="The Escort"),
    Trait("Caster", verb="be a", eff1=Effect("special", "rest shield", 1), archetype="The Bride"), #?
    Trait("Driven", verb="be", eff1=Effect("boost", "max energy", 0.2), eff2=Effect("boost", "energy", 0.1), archetype="The Player"),
    Trait("Country girl", verb="be a", eff1=Effect("special", "all farm weaknesses", 1), eff2=Effect("boost", "farm preference increase", 0.5), archetype="The Maid"),
    Trait("Noble", verb="be a", eff1=Effect("boost", "prestige", 2), archetype="The Courtesan"),
    Trait("Naturist", verb="be a", eff1=Effect("special", "naked", 1), archetype="The Model", base_description = "She has no shame showing her naked body to perfect strangers."),
    Trait("Vicious", verb="be", effects=[Effect("change", "service", 5), Effect("change", "sex", 5), Effect("change", "anal", 5), Effect("change", "fetish", 5)], archetype="The Escort"),
    Trait("Conduit", verb = "be a", eff1 = Effect("change", "mojo cost", -1), archetype="The Fox"), #?

    Trait("Dynamo", verb = "be a", effects = [Effect("boost", "max energy", 0.3), Effect("boost", "energy", 0.15)], base_description = "Burns with fiery energy.", public=False, archetype="The Fox"),
    Trait("Lolita", verb = "be a", effects = [Effect("boost", "tip", 2, chance=0.2)], base_description = "She isn't actually underage, but looks like she is - and some customers love that.", public=False, archetype="The Player"),
    Trait("Ghost", verb = "be a", effects = [Effect("special", "immune", 1)], base_description = "She is a ghost, and cannot be hurt by any normal means.", public=False, archetype="The Escort"),
    Trait("Stalwart", verb = "be", effects = [Effect("change", "all skill max", 10, scales_with = "rank")], base_description = "It doesn't matter what she does, she'll train harder than anyone else.", public=False, archetype="The Bride"),
]

pos_traits = [
    Trait("Cute", verb = "be", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model"),
    Trait("Long legs", verb = "have", eff1 = Effect("change", "beauty", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Player"),
    Trait("Nice boobs", verb = "have", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Escort"),
    Trait("Juicy ass", verb = "have a", eff1 = Effect("change", "body", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"),
    Trait("Sweet", verb = "be", eff1 = Effect("change", "charm", 5, scales_with = "rank"), eff2 = Effect("personality", "sweet"), archetype="The Bride"),
    Trait("Exotic", verb = "be", eff1 = Effect("change", "charm", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Fox"),
    Trait("Polite", verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan"),
    Trait("Feminine", verb = "be", eff1 = Effect("change", "refinement", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Model"),
    Trait("Horny", verb = "be", eff1 = Effect("change", "libido", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"),
    Trait("Resilient", verb = "be", eff1 = Effect("change", "constitution", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Maid"),
    Trait("Delicate", verb = "be", eff1 = Effect("change", "sensitivity", 5, scales_with = "rank"), eff2 = Effect("gain", "reputation", 5), archetype="The Bride"),
    Trait("Meek", verb = "be", eff1 = Effect("change", "obedience", 5, scales_with = "rank"), eff2 = Effect("personality", "meek"), archetype="The Maid"),

    Trait("Pretty eyes", verb = "have", eff1 = Effect("change", "beauty", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Model"), #!
    Trait("Firm tits", verb = "have", eff1 = Effect("change", "body", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Slut"), #!
    Trait("Seductive", verb = "be", eff1 = Effect("change", "charm", 10), eff2 = Effect("gain", "reputation", 5), eff3 = Effect("personality", "superficial"), archetype="The Model"), #!
    Trait("Graceful", verb = "be", eff1 = Effect("change", "refinement", 10), eff2 = Effect("gain", "reputation", 5), archetype="The Courtesan"), #!

    Trait("Beautiful", verb = "be", eff1 = Effect("boost", "beauty gains", 0.25), archetype="The Model"),
    Trait("Fit", verb = "be", eff1 = Effect("boost", "body gains", 0.25), archetype="The Escort"),
    Trait("Charming", verb = "be", eff1 = Effect("boost", "charm gains", 0.25), archetype="The Fox"),
    Trait("Elegant", verb = "be", eff1 = Effect("boost", "refinement gains", 0.25), archetype="The Courtesan"),
    Trait("Slutty", verb = "be", eff1 = Effect("boost", "libido gains", 0.25), archetype="The Slut"),
    Trait("Athletic", verb = "be", eff1 = Effect("boost", "constitution gains", 0.25), archetype="The Player"),
    Trait("Sensitive", verb = "be", eff1 = Effect("boost", "sensitivity gains", 0.25), archetype="The Bride"),
    Trait("Obedient", verb = "be", eff1 = Effect("boost", "obedience gains", 0.25), archetype="The Maid"),

    Trait("Energetic", verb = "be", eff1 = Effect("boost", "max energy", 0.1), archetype="The Player"), ## This is a 10% increase
    Trait("Tough", verb = "be", eff1 = Effect("boost", "hurt", -0.33), archetype="The Maid"),
    Trait("Sexy", verb = "be", eff1 = Effect("boost", "reputation gains", 0.2), archetype="The Escort"),
    Trait("Humble", verb = "be", eff1 = Effect("boost", "upkeep", -0.2), archetype="The Maid"),

    Trait("Virgin", verb = "be a", eff1 = Effect("special", "virgin", 1), eff2 = Effect("change", "all sex acts requirements", 10), archetype="The Bride", base_description = "This girl is a virgin."), # Special trait, goes away after 1st sex
    Trait("Sharp", verb = "be", eff1 = Effect("boost", "xp gains", 0.1), eff2 = Effect("personality", "nerd"), archetype="The Fox"),
    Trait("Loyal", verb = "be", eff1 = Effect("boost", "love gains", 0.1), archetype="The Bride"),
    Trait("Brave", verb = "be", eff1 = Effect("boost", "fear", -0.1), archetype="The Escort"),
    Trait("Strong", verb = "be", eff1 = Effect("change", "defense", 2), archetype="The Player"),
    Trait("Lucky", verb = "be", eff1 = Effect("special", "lucky", 1), archetype="The Fox", base_description = "She's up all night..."),

    Trait("Deft", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Maid"),
    Trait("Nimble", verb = "be", eff1 = Effect("boost", "dancer jp gains", 0.1), eff2 = Effect("boost", "geisha jp gains", 0.1), archetype="The Player"),
    Trait("Soft skin", verb = "have", eff1 = Effect("boost", "geisha jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Courtesan"),
    Trait("Bright", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "geisha jp gains", 0.1), archetype="The Courtesan"),
    Trait("Agile", verb = "be", eff1 = Effect("boost", "dancer jp gains", 0.1), eff2 = Effect("boost", "masseuse jp gains", 0.1), archetype="The Fox"),
    Trait("Brisk", verb = "be", eff1 = Effect("boost", "waitress jp gains", 0.1), eff2 = Effect("boost", "dancer jp gains", 0.1), archetype="The Model"),

    Trait("Rowdy", verb = "be", effects = [Effect("boost", "waitress jp gains", 0.2), Effect("increase satisfaction", "waitress", 1), Effect("increase satisfaction", "geisha", -2)], opposite=['Modest', 'Unhurried'], archetype="The Slut"),
    Trait("Powerful", verb = "be", effects = [Effect("boost", "dancer jp gains", 0.2), Effect("increase satisfaction", "dancer", 1), Effect("increase satisfaction", "masseuse", -2)], opposite=['Modest', 'Unhurried'], archetype="The Bride"),
    Trait("Unhurried", verb = "be", effects = [Effect("boost", "masseuse jp gains", 0.2), Effect("increase satisfaction", "masseuse", 1), Effect("increase satisfaction", "waitress", -2)], opposite=['Powerful', 'Rowdy'], archetype="The Escort"),
    Trait("Modest", verb = "be", effects = [Effect("boost", "geisha jp gains", 0.2), Effect("increase satisfaction", "geisha", 1), Effect("increase satisfaction", "dancer", -2), Effect("personality", "meek")], opposite=['Rowdy', 'Powerful'], archetype="The Fox"),

    Trait("Sensual", verb = "be", eff1 = Effect("boost", "service jp gains", 0.1), eff2 = Effect("boost", "sex jp gains", 0.1), eff3 = Effect("personality", "pervert"), archetype="The Escort"),
    Trait("Kinky", verb = "be", eff1 = Effect("boost", "anal jp gains", 0.1), eff2 = Effect("boost", "fetish jp gains", 0.1), eff3 = Effect("personality", "masochist"), archetype="The Player"),
    Trait("Pervert", verb = "be a", eff1 = Effect("change", "all sex acts requirements", -10), eff2 = Effect("personality", "pervert"), archetype="The Slut"),
    Trait("Thief", verb = "be a", eff1 = Effect("special", "pickpocket", 1), archetype="The Fox", base_description = "She may steal a little amount from the customers while seducing them. Reputation may suffer."),
    Trait("Sane", verb = "be", eff1 = Effect("change", "sanity loss", -1), archetype="The Courtesan"),
    Trait("Trusting", verb = "be", eff1 = Effect("change", "fear per day", -1, chance=0.25), archetype="The Maid"),
    Trait("Loving", verb = "be", eff1 = Effect("change", "love per day", 1, chance=0.25), archetype="The Bride"),

    ]
neg_traits = [
    Trait("Plain", verb = "be", eff1 = Effect("change", "beauty", -10, scales_with = "rank"), opposite = "Cute"),
    Trait("Scars", verb = "have", eff1 = Effect("change", "body", -10, scales_with = "rank"), opposite = "Nice boobs"),
    Trait("Mean", verb = "be", eff1 = Effect("change", "charm", -10, scales_with = "rank"), opposite = "Sweet"),
    Trait("Rude", verb = "be", eff1 = Effect("change", "refinement", -10, scales_with = "rank"), opposite = "Polite"),
    Trait("Cold", verb = "be", eff1 = Effect("change", "libido", -10, scales_with = "rank"), eff2 = Effect("personality", "cold"), opposite = "Horny"),
    Trait("Weak", verb = "be", eff1 = Effect("change", "constitution", -10, scales_with = "rank"), opposite = "Resilient"),
    Trait("Rough", verb = "be", eff1 = Effect("change", "sensitivity", -10, scales_with = "rank"), opposite = "Delicate"),
    Trait("Defiant", verb = "be", eff1 = Effect("change", "obedience", -10, scales_with = "rank"), opposite = "Meek"),

    Trait("Scruffy", verb = "be", eff1 = Effect("boost", "beauty gains", -0.5), opposite = "Beautiful"),
    Trait("Plump", verb = "be", eff1 = Effect("boost", "body gains", -0.5), opposite = "Fit"),
    Trait("Timid", verb = "be", eff1 = Effect("boost", "charm gains", -0.5), opposite = "Charming"),
    Trait("Vulgar", verb = "be", eff1 = Effect("boost", "refinement gains", -0.5), opposite = "Elegant"),
    Trait("Tame", verb = "be", eff1 = Effect("boost", "libido gains", -0.5), opposite = "Slutty"),
    Trait("Frail", verb = "be", eff1 = Effect("boost", "constitution gains", -0.5), opposite = "Athletic"),
    Trait("Jaded", verb = "be", eff1 = Effect("boost", "sensitivity gains", -0.5), opposite = "Sensitive"),
    Trait("Rebellious", verb = "be", eff1 = Effect("boost", "obedience gains", -0.5), eff2 = Effect("personality", "rebel"), opposite = "Obedient"),

    Trait("Lazy", verb = "be", eff1 = Effect("boost", "max energy", -0.15), opposite = ["Energetic", "Driven"]),
    Trait("Sickly", verb = "be", eff1 = Effect("boost", "hurt", +2), opposite = "Tough"),
    Trait("Homely", verb = "be", eff1 = Effect("boost", "reputation gains", -0.25), opposite = "Sexy"),
    Trait("Expensive", verb = "be", eff1 = Effect("boost", "upkeep", 0.25), opposite = "Humble"),

    Trait("Slow", verb = "be", eff1 = Effect("boost", "xp gains", -0.25), opposite = ["Fast learner", "Sharp"]),
    Trait("Disloyal", verb = "be", eff1 = Effect("boost", "love gains", -0.25), opposite = "Loyal"),
    Trait("Fearful", verb = "be", eff1 = Effect("boost", "fear", 0.25), opposite = "Brave"),
    Trait("Vulnerable", verb = "be", eff1 = Effect("change", "defense", -2), opposite = ["Strong", "Warrior"]),
    Trait("Unlucky", verb = "be", eff1 = Effect("special", "unlucky", 1), base_description = "She shouldn't have broken that magic mirror... Increased chance of critical failure when working.", opposite = "Lucky"),

    Trait("All thumbs", verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("increase satisfaction", "waitress", -1), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy']),
    Trait("Awkward", verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("increase satisfaction", "dancer", -1), opposite=['Nimble', 'Agile', 'Brisk', 'Powerful']),
    Trait("Brutal", verb = "be", eff1 = Effect("boost", "masseuse jp gains", -0.5), eff2 = Effect("increase satisfaction", "masseuse", -1), opposite=['Deft', 'Soft skin', 'Agile', 'Unhurried']),
    Trait("Dumb", verb = "be", eff1 = Effect("boost", "geisha jp gains", -0.5), eff2 = Effect("increase satisfaction", "geisha", -1), opposite=['Nimble', 'Soft skin', 'Bright', 'Modest']),
    Trait("Oafish", verb = "be", eff1 = Effect("boost", "dancer jp gains", -0.5), eff2 = Effect("boost", "geisha jp gains", -0.5), opposite=['Nimble', 'Agile', 'Brisk', 'Soft skin', 'Bright']),
    Trait("Clumsy", verb = "be", eff1 = Effect("boost", "waitress jp gains", -0.5), eff2 = Effect("boost", "masseuse jp gains", -0.5), opposite=['Deft', 'Bright', 'Brisk', 'Rowdy', 'Soft skin', 'Agile']),

    Trait("Prude", verb = "be", eff1 = Effect("boost", "service jp gains", -0.5), eff2 = Effect("boost", "sex jp gains", -0.5), opposite = "Naughty"),
    Trait("Naive", verb = "be", eff1 = Effect("boost", "anal jp gains", -0.5), eff2 = Effect("boost", "fetish jp gains", -0.5), opposite = "Kinky"),
    Trait("Square", verb = "be", eff1 = Effect("change", "all sex acts requirements", 25), opposite = "Pervert"),
    Trait("Insane", verb = "be", eff1 = Effect("change", "sanity loss", 1), opposite = "Sane"),

    Trait("Distrustful", verb = "be", eff1 = Effect("change", "fear per day", 1, chance=0.25), opposite = "Trusting"),
    Trait("Spiteful", verb = "be", eff1 = Effect("change", "love per day", -1, chance=0.25), opposite = "Loving"),

    Trait("Earthbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),
    Trait("Waterbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),
    Trait("Voidbound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),
    Trait("Firebound", verb = "be", effects = [Effect("special", "bound", 1), Effect("change", "defense", 6)], base_description = "Will not attack you. Deadly to everyone else.", public=False),
    ]
    
all_traits = gold_traits + pos_traits + neg_traits

all_traits.append(Trait("Godless", verb = "be", eff1 = Effect("boost", "reputation gains", -0.2)))

all_traits.append(Trait("Housebroken", verb="be", effects = [Effect("change", "job obedience target", -10), Effect("change", "whore obedience target", -10)], base_description = "She lost her virginity in a brothel. This is all she knows."))

all_traits.append(Trait("Teacher's pet", verb="be a", effects = [Effect("change", "train obedience target", -20), Effect("boost", "love", 0.2)], base_description = "Her first time was with you. You're special to her."))

all_traits.append(Trait("Trauma", verb="have a", effects = [Effect("change", "obedience", 15), Effect("change", "libido", -15), Effect("boost", "fear", 0.2)], base_description = "She lost her virginity against her will, and has to live with the trauma."))

all_traits.append(Trait("Farmgirl", verb="be a", effects = [Effect("change", "obedience", 10), Effect("boost", "farm preference increase", 0.25)], base_description = "She has lost her virginity in the farm like a filthy animal."))

all_traits.append(Trait("Mark of Chaos", verb="have a", effects = [Effect("boost", "sanity loss", -0.33)], base_description = "She lost her virginity in a strange feverish dream, yet emerged with reinforced sanity."))

fields = ["name", 'base_description', 'eff1', 'value1', 'eff2', 'value2', 'eff3', 'value3']

if __name__ == "__main__":
    writer = csv.writer(sys.stdout)
    
    writer.writerow(fields)
    for t in all_traits:
        writer.writerow(t.to_list())