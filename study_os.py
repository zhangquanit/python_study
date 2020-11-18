# coding=utf-8
import os
import re
import time
import sys, getopt
import platform


def getUsageStr():
    tipStr = ('Usage: \n releaseApk.py -m <message> -e <env> -r <apkReceiverEmail>\n'
              + ' -m, --message <message> 打包日志信息 \n'
              + ' -e, --env <env>  打包环境：[qa,online,dev], 不传默认为qa。\n'
              + ' -r, --apkReceiverEmail <apkReceiverEmail> '
              + '基准包的接收者的邮件（乐固加固后的未签名apk，由发包者用脚本打渠道包）,不传则生成medlinker渠道上传到蒲公英\n'
              + ' -l, --isLiteApp <isLiteApp> 是否是执业版：[ture,false]，不传用android项目默认配置 。\n'
              + ' noemail  不发邮件，默认要发送（上传蒲公英后）。\n'
              + ' local  不发邮件，不上传蒲公英。\n'
              + ' jiagu  打包完成后，自动上传加固并下载\n'
              + ' haveOutputApk  已经打包apk成功，不需要再次打包（qa、online有效，online包需要加固）。\n'
              + ' haveLeguApk 已经打包apk成功，并已获取加固未签名的apk（online有效）。')
    return (tipStr)


if __name__ == '__main__':  # 内置的变量 __name__，当该模块被直接执行的时候，__name__ 等于文件名.
    argv = sys.argv[1:]  # 所有命令行参数以空格为分隔符，都保存在了sys.argv列表中。其中第1个为脚本的文件名。
    print(argv)

    message = ''
    buildEnv = 'qa'
    apkReceiverEmail = 'no'
    isLiteApp = None
    try:
        # 这里的 h 就表示该选项无参数，冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
        opts, args = getopt.getopt(argv, "hm:e:r:l:", ["message=", "env=", "apkReceiverEmail=", "isLiteApp"])
    except getopt.GetoptError:
        print(getUsageStr())
        sys.exit(2)

    print("-----------")
    print(opts)
    print(args)
    print("------------")
    for opt, arg in opts:
        if opt == '-h':
            print(getUsageStr())
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg
            print('-m arg =%s' % arg)
        elif opt in ("-e", "--env"):
            buildEnv = arg
            print('-e arg =%s' % arg)
        elif opt in ("-r", "--apkReceiverEmail"):
            apkReceiverEmail = arg
            print('-r arg =%s' % arg)
        elif opt in ("-l", "--isLiteApp"):
            isLiteApp = arg
            print('-l arg =%s' % arg)

    print('message = %s, buildEnv = %s, apkReceiverEmail = %s, isLiteApp = %s' % (
        message, buildEnv, apkReceiverEmail, isLiteApp))

    if ('haveOutputApk' in sys.argv):
        print("已经打包apk成功，不重新打包")
    elif ('haveLeguApk' in sys.argv):
        print("已经获取加固apk，不重新打包")
    elif ("jiagu" in sys.argv):
        print("startJiaGu()")
    else:
        print("updateGitRepo()")
        print("exeGradleCmd(buildEnv, isLiteApp)")

    if ("jiagu" not in sys.argv):
        # online包需要加固
        if buildEnv == 'online':
            print("dealApkAndSendPgy(buildEnv, message)")

        elif buildEnv == 'qa' or buildEnv == 'dev':
            print("buildEnv == 'qa' or buildEnv == 'dev'")
            # uploadApkPatch = 'app/build/outputs/apk/online/release/app-online-release.apk'
            # uploader = PgyUploader()
            # uploader.uploadPgyer(uploadApkPatch, buildEnv, message)
