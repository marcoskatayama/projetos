import Mail from "nodemailer/lib/mailer";
import { IMailProvider, IMessage } from "../IMailProvider";
import nodemailer from 'nodemailer'

export class MailTrapMailProvider implements IMailProvider{
    private transporter: Mail;

    constructor(){
        this.transporter = nodemailer.createTransport({
            host: 'smtp:mailtrap.io',
            port: 2525,
            auth: {
                user: 'sd56d4fsd2fd',
                pass: 'sdajiksdf45d'
            }
        })
    }

    async sendMail(messagem: IMessage): Promise<void> {
        await this.transporter.sendMail({
            to:{
                name: messagem.to.name,
                address: messagem.to.email
            },
            from:{
                name: messagem.from.name,
                address: messagem.from.email
            },
            subject: messagem.subject,
            html: messagem.body
        })
    }
}